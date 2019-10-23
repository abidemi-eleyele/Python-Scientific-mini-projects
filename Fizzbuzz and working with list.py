pulses = [1601, 1596, 1596, 1598, 1599, 1598, 1598, 1599, 1599, 1599, 1594, 1586, 1572, 1550, 1525, 1503, 1489, 1482,
          1479, 1475, 1470, 1465, 1463, 1471, 1490, 1503, 1516, 1526, 1532, 1536, 1537, 1545, 1553, 1561, 1563, 1561,
          1556, 1550, 1544, 1544, 1545, 1554, 1562, 1566, 1568, 1571, 1576, 1579, 1578, 1581, 1581, 1583, 1583, 1587,
          1585, 1588]
print(len(pulses))
print(pulses[0])
# print(pulses[100])
sum = 0
for p in pulses:
    # print(p)
    sum = sum + p
average = sum / len(pulses)
print('Sum of pulses is :', sum)
print('Average of the pulses is :', average)


def summer(mylist):
    sum = 0
    for p in mylist:
        # print(p)
        sum = sum + p
    average = sum / len(mylist)

    return average


mylist = pulses
average = summer(pulses)
print(average)
print(pulses[-1])
print(pulses[0:9])

import statistics as st

average = st.mean(pulses)
print('statistics mean is:', average)
import numpy as np

sum_new = np.sum(pulses)
print('statistics sum is:', sum_new)

# def FizzBuzz (count):
"""for num in range(0, 100):
    if num % 5 == 0 and num % 7 == 0:
            print('python')
    elif num % 5 == 0:
            print('spam')
    elif num % 7 == 0:
            print('eggs')
    else:
            print(num)"""

def FizzBuzz(limit):
    for num in range(limit):
        if num % 5 == 0 and num % 7 == 0:
            print('python')
        elif num % 5 == 0:
            print('spam')
        elif num % 7 == 0:
            print('eggs')
        else:
            print(num)
FizzBuzz(50)
