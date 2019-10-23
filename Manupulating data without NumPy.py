# import csv
import math
def myfunc(number):
    if number == '':
        return(math.nan)
    else:
        return float (number)

with open ("EbbasData_clean.csv", 'r') as ebba:
    #  print(ebba.readline())
    lines = ebba.readlines ()
times = []
pressures_abs = []
temps = []
volumes = []
for line in lines [3:243]:
    parts = line.split (',')
    times.append(myfunc(parts[1]))
    pressures_abs.append(myfunc(parts[2]))
    temps.append(myfunc(parts[3]))
    volumes.append(myfunc(parts[10]))
print (times)
print (len (times))
print (pressures_abs)
print (len (pressures_abs))
print (temps)
print (len (temps))
print (volumes)
print (len (volumes))

import matplotlib.pyplot as plt
...
plt.plot (temps)
plt.title ('Temperature plot')
plt.ylabel ('temps')
plt.xlabel ('time')
plt.savefig ('Temp_vs_time.jpg')
plt.show ()

# Create plots with pre-defined labels.
fig, ax = plt.subplots ()
ax.plot (times, pressures_abs, 'b', label='Absolute Pressure')
ax.plot (times, volumes, 'g', label='Volumes')
ax.plot (times, temps, 'r', label='Temperature')
plt.xlabel ('Time')
plt.ylabel ('Pressure,volume and temprature')
legend = ax.legend (loc='upper center', shadow=True, fontsize='x-large')
# Put a nicer background color on the legend.
legend.get_frame ().set_facecolor ('C0')
plt.savefig ('P&V&T.png')
plt.show ()


#    if parts [1] == '':
#        times.append (math.nan)
#    else:
#        time = float (parts [1])
#        times.append(time)
#    if parts [2] == '':
#        pressures_abs.append (math.nan)
#    else:
#        pressure = float (parts [2])
#        pressures_abs.append (pressure)
#    if parts [3] == '':
#        temps.append (math.nan)
#    else:
#        temp = float (parts [3])
#        temps.append (temp)
#    if parts [10] == '':
#        volumes.append (math.nan)
#    else:
#        volume = float (parts [10])
#        volumes.append (volume)

# times.append(parts[1])

# if parts[2] == '':
#   pressures_abs.append(math.nan)
# else :
#   pressure = float(parts[2])
#  pressures_abs.append(pressure)

# temps.append(parts[3])
# volumes.append(parts[10])


# for line in lines[3:240]:
#   parts = line.split(',')
#  print(parts[2])


# for line in lines:
#   line.split()
# reader = csv.reader(ebba)
# '''for row in reader:
#   print(row[0], end='\t\t')
#  print(row[1], end = '\t\t')
# print(row[2], end = '\t\t')
# print(row[3], end='\t\t')
# print(row[4], end='\t\t')
# print(row[5], end='\n')'''
