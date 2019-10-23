import matplotlib.pyplot as plt
N = 10                                                  # number of first 10 elements in the row
CONV_FACTOR = 0.6 / (2 ** 10 - 1)                       # voltage conversion factor

def vol_conv_func(reading):
    return float (reading) * CONV_FACTOR                # function for converting readings to voltage

with open ("pulses.csv", 'r') as pulses:                # load the pulses csv file
    lines = pulses.readlines ()
    print (pulses.readline ())

timestamps = []
list_of_lists = []
corr_list_of_list = []

def baseline(inputList):                                # baseline correction function
    average = sum(inputList [:N])/N
    for i in range(len(inputList)):
        inputList[i] -= average
    return inputList

for line in lines:
    parts = line.split (',')                            # split the csv into parts
    timestamps.append (float (parts [0]))               # parts[0] appended to timestamps
    detector_readings = []
    for col in parts [1:]:
        detector_readings.append (vol_conv_func (col))  # append the converted reading to detector readings
    list_of_lists.append (detector_readings)            # append detector reading to make list of list

list_of_sum = []
for list in list_of_lists:
    corrected_values = baseline (list)                  # corrected
    list_of_sum.append (sum (corrected_values))
    corr_list_of_list.append (corrected_values)

plt.plot (list_of_lists [0])                            # single pulse plot from the first row of list of list before correction
plt.title ('First pulse')
plt.ylabel ('Voltage')
plt.xlabel ('time')
plt.savefig ('First_pulse.jpg')
plt.show ()

plt.plot (corr_list_of_list [0])                        # corrected single pulse plot
plt.title ("Correst first pulse")
plt.ylabel ('Voltage')
plt.xlabel ('time')
plt.savefig ('Corrected_First_pulse.jpg')
plt.show ()

plt.hist (list_of_sum, bins=20)                         # histogram plot of corrected list
plt.title ('Histogram of Corrected list')
plt.ylabel ('Number of readings')
plt.xlabel ('Corrected Voltages')
plt.savefig ('Historgram plot.jpg')
plt.show ()
plt.clf()

plt.imshow (corr_list_of_list, aspect='auto', cmap='twilight') # corrected baseline values plot
plt.savefig ('Baseline correction.jpg')
plt.show ()