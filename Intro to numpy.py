from math import pi
import time
import numpy as np
arr1 = np.loadtxt(fname = 'EbbasData_clean.csv', delimiter = ',', skiprows= 3, dtype = str, usecols = range(1,11))
arr1_where_empty = arr1 == ''
arr1[arr1_where_empty] =np.nan
arr1 = arr1.astype(float)
import matplotlib.pyplot as plt
...
plt.plot (arr1[:,0], arr1[:,2])
plt.title ('Temperature(numpy style) plot')
plt.ylabel ('temps')
plt.xlabel ('time')
plt.savefig ('Temperature plot by numpy1.jpg')
plt.show ()
d = np.arange(0, 2, 10)
e = np.linspace(0, 2, 10)
print (time.time())
print (time.localtime(time.time()))

x = d
y = e
x_1, y_1 = np.meshgrid(x, y)
print('x_1 = ')
print(x_1)
print('y_1 = ')
print(y_1)
#ellipse = x*x*2 +4*y*y*2
#plt.contourf(x_1, y_1, ellipse, cmap = 'jet')
#plt.colorbar()
#plt.show()