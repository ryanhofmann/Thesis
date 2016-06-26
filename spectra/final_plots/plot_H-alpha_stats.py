#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
time = np.array([72, 96, 111, 121, 154, 196, 240, 405, 463])
narrow = [0, 2, 3, 4, 7]
eqwidth = np.array([97.8, 90.2, 181, 221, 500, 767, 1190, 1552, 921])
fwhm = np.array([1400, 2300, 2800, 3150, 3500, 3450, 3500, 2700, 2750])
flux = np.array([1.456, .7295, 1.915, 2.669, 3.651, 4.731, 3.624, 1.264, .6692])*1e-13
v_abs = np.array([70, 67, 80, 70, 73])
plt.subplot(221)
err = np.zeros(len(eqwidth)) + 10.
plt.errorbar(time, eqwidth, yerr=err, marker='o', linestyle='--', color='r')
plt.xlabel('Days')
plt.ylabel('$\AA$')
plt.text(20, 1400, '(a)')
plt.text(200, 100, r'H$\alpha$ EW')
plt.xlim(0, 500)
plt.ylim(0, 1600)
plt.subplot(222)
err = np.zeros(len(flux)) + 1e-14
plt.errorbar(time, flux, yerr=err, marker='o', linestyle='--', color='y')
plt.xlabel("Days")
plt.ylabel("erg s$^{-1}$ cm$^{-2}$")
plt.text(20, 4.375e-13, '(b)')
plt.text(200, 0.3125e-13, r'H$\alpha$ Flux')
plt.xlim(0, 500)
plt.ylim(0, 5e-13)
plt.subplot(223)
err = np.zeros(len(fwhm)) + 100.
plt.errorbar(time, fwhm, yerr=err, marker='o', linestyle='--', color='g')
plt.xlabel('Days')
plt.ylabel('km s$^{-1}$')
plt.text(20, 3500, '(c)')
plt.text(200, 250, r'H$\alpha$ FWHM')
plt.xlim(0, 500)
plt.ylim(0, 4000)
plt.subplot(224)
err = np.zeros(len(v_abs)) + 5.
plt.errorbar(time[narrow], v_abs, yerr=err, marker='o', linestyle='--', color='b')
plt.xlabel('Days')
plt.ylabel('km s$^{-1}$')
plt.text(20, 87.5, '(d)')
plt.text(200, 6.25, r'H$\alpha$ P-Cygni width')
plt.xlim(0, 500)
plt.ylim(0, 100)
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.show()
