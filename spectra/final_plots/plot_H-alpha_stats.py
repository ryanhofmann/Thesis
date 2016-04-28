#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
time = np.array([67, 91, 106, 116, 149, 191, 235, 400, 458])
narrow = [0, 2, 3, 4, 7]
eqwidth = np.array([97.8, 90.2, 181, 221, 500, 767, 1190, 1552, 921])
fwhm = np.array([1400, 2300, 2800, 3150, 3500, 3450, 3500, 2700, 2750])
v_abs = np.array([70, 67, 80, 70, 73])
plt.subplot(311)
plt.plot(time, eqwidth, 'r--', time, eqwidth, 'ro')
plt.xlabel('Days since discovery')
plt.ylabel('Equivalent width ($\AA$)')
plt.xlim(0, 500)
plt.ylim(0, 1600)
plt.subplot(312)
plt.plot(time, fwhm, 'y--', time, fwhm, 'yo')
plt.xlabel('Days since discovery')
plt.ylabel('FWHM (km s$^{-1}$)')
plt.xlim(0, 500)
plt.ylim(0, 4000)
plt.subplot(313)
plt.plot(time[narrow], v_abs, 'b--', time[narrow], v_abs, 'bo')
plt.xlabel('Days since discovery')
plt.ylabel('$\Delta$v (km s$^{-1}$)')
plt.xlim(0, 500)
plt.ylim(0, 100)
plt.show()
