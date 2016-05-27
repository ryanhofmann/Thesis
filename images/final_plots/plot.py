#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# Define plotting function
def plot(infile, multi=1):

  # Import data from text file
  data = np.genfromtxt(infile, skip_header=1)

  # Define arrays for plotting
  x = data[:, 0]
  ycols = [1, 3, 5, 7, 9, 11, 13]
  filters = ['B', 'V', 'R', 'I', 'J', 'H', 'K']
  y = data[:, ycols]
  single = 2 # Column of red magnitudes
  yerrcols = [2, 4, 6, 8, 10, 12, 14]
  yerr = data[:, yerrcols]
  xerr = np.zeros(len(x))
  D = 32.8 # Distance modulus

  # Determine range for y-axes
  ymin = np.min(y[np.where(y != 0)])
  ymax = np.max(y[np.where(y != 0)])
  pad = 0.1*(ymax - ymin)
  ymin -= pad; ymax += pad

  # Plot data with two y-scales
  fig, ax1 = plt.subplots()
  if multi:
    for i in range(0, len(ycols)):
      ind = np.where(y[:, i] != 0)
      xi, yi, xierr, yierr = x[ind], y[:, i][ind], xerr[ind], yerr[:, i][ind]
      phot = ax1.errorbar(xi, yi, yierr, xierr, marker='o', linestyle='-')
      color = phot[0].get_color()
      plt.text(90, yi[1], filters[i], size=10, color=color)
  else:
    ind = np.where(y[:, single] != 0)
    xi, yi, xierr, yierr = x[ind], y[:, single][ind], xerr[ind], yerr[:, single][ind]
    ax1.errorbar(xi, yi, yierr, xierr, marker='o', linestyle='-', color='red')

  # Plot spectra dates
  spec_dates = np.array([67, 91, 106, 116, 149, 191, 235, 400, 458])
  spec_height = np.zeros(len(spec_dates)) + ymin + 0.5*pad
  plt.plot(spec_dates, spec_height, marker='|', mew=2, linestyle='None', color='brown')
  plt.text(260, spec_height[0]+0.1, "spectral epochs", fontsize=10, color="brown")

  # Format axes and display
  ax1.set_xlabel('Days since discovery')
  ax1.set_ylabel('Apparent magnitude')
  ax1.set_xlim(-10, 500)
  ax1.set_ylim(ymax, ymin)
  ax2 = ax1.twinx()
  ax2.set_ylim(ymax - D, ymin - D)
  ax2.set_ylabel('Absolute magnitude')
  plt.show()
