#!/usr/bin/python

# Define function for plotting all spectra
def specplot(xmin=0, xmax=0, vel=0, narrow=0, scale='lin', shift=0, stretch=0, x_label=6300, y_label=0.25, d_label=1):

  import numpy as np
  import matplotlib.pyplot as plt
  import os

  # Get list of spectra
  spectra = []
  for item in os.listdir('.'):
    if item.startswith('201') and item.endswith('.txt'):
      spectra.append(item)

  # Sort spectra by date
  spectra.sort()

  # Read spectra into arrays
  xyarr = []
  delta = [-2.7, 1.0, -3.2, -3.6, -0.1, -1.0, 0.0, -2.5, 0.0]
  c = ['darkred', 'red', 'orange', 'y', 'green', 'cyan', 'blue', 'purple', 'magenta']
  days = [72, 96, 111, 121, 154, 196, 240, 405, 463]
  no = []
  for i in range(len(spectra)):
    if narrow and 'MMT' not in spectra[i]:
      no.append(i)
      continue
    arr = np.genfromtxt(spectra[i])
    xyarr.append(arr)
  j = 0
  for ind in no:
    del delta[ind-j]
    del c[ind-j]
    del days[ind-j]
    j += 1

  # Align spectra, max = 656.3 nm
  for i in range(0, len(xyarr)):
#    wmax = np.argmax(xyarr[i], axis=0)[1]
#    delta = xyarr[i][wmax,0] - 6563.
    xyarr[i][:,0] = np.subtract(xyarr[i][:,0], delta[i])

  # Normalize spectra
  cal = 6300.
  no = 0
  for i in range(0, len(xyarr)):
    idx = np.abs(xyarr[i][:, 0] - cal).argmin()
    idxmin, idxmax = idx - 5, idx + 5
    xmean = np.mean(xyarr[i][idxmin:idxmax, 1])
    xyarr[i][:, 1] /= xmean

  # Format spectra for plotting
  if stretch > 0:
    for i in range(0, len(xyarr)):
      xyarr[i][:,1] = 1. + (xyarr[i][:,1] - 1.)*(stretch*(i+1))
  if shift > 0:
    base = []
    for i in range(0, len(xyarr)):
      if scale == 'log':
        base.append(shift**i)
        xyarr[i][:,1] *= base[i]
      else:
        base.append(shift*i)
        xyarr[i][:,1] += base[i]

  # If velocity, convert spectra using relativistic doppler formula
  if vel:
    for i in range(0, len(xyarr)):
      z = xyarr[i][:,0]/6563.
      beta = (np.square(z) - 1)/(np.square(z) + 1)
      xyarr[i][:,0] = 3e5*beta

  # Plot spectra
  for i in range(0, len(xyarr)):
    plt.plot(xyarr[i][:,0], xyarr[i][:,1], color=c[i])
    ybase = np.zeros(len(xyarr[i][:,0])) + 1.
    if shift > 0:
      if scale == 'log':
        ybase *= shift**i
      else:
        ybase += shift*i
#    plt.plot(xyarr[i][:,0], ybase, color=c[i])

  # Configure axes and labels
  if xmin != 0 or xmax != 0:
    plt.xlim(xmin, xmax)
  if scale == 'log':
    plt.yscale('log')
  if vel:
    plt.xlabel('velocity (km/s)')
  else:
    plt.xlabel(r'wavelength ($\AA$)')
  if scale == 'log':
    plt.ylabel(r'log F$_\lambda$ (scaled)')
  else:
    plt.ylabel(r'F$_\lambda$ (scaled)')

  # Label spectra
  if shift > 1:
    for i in range(0, len(xyarr)):
      if 'MMT' in spectra[i]:
        plt.text(x_label, shift**(d_label*i+y_label), str(days[i])+'$^{i}$', color=c[i])
        if '2016' not in spectra[i]:
          if vel:
            plt.text(11600, shift**(d_label*i+y_label), '$\oplus$', color='brown')
          else:
            plt.text(6840, shift**(d_label*i+y_label), '$\oplus$', color='brown')
      if 'LBT' in spectra[i]:
        plt.text(x_label, shift**(d_label*i+y_label), str(days[i])+'$^{ii}$', color=c[i])
        if vel:
          plt.text(11600, shift**(d_label*i+y_label), '$\oplus$', color='brown')
          plt.text(43500, shift**(d_label*i+2.*y_label), '$\oplus$', color='brown')
        else:
          plt.text(6840, shift**(d_label*i+y_label), '$\oplus$', color='brown')
          plt.text(7550, shift**(d_label*i+2.*y_label), '$\oplus$', color='brown')
      if 'Berkeley' in spectra[i]:
        plt.text(x_label, shift**(d_label*i+y_label), str(days[i])+'$^{iii}$', color=c[i])
      if 'Bok' in spectra[i]:
        plt.text(x_label, shift**(d_label*i+y_label), str(days[i])+'$^{iv}$', color=c[i])
        if vel:
          plt.text(43500, shift**(d_label*i+3.5*y_label), '$\oplus$', color='brown')
        else:
          plt.text(7550, shift**(d_label*i+3.5*y_label), '$\oplus$', color='brown')
  plt.show()
