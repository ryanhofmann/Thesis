#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# Import spectrum
def spec_import(infile):

  # Get Berkeley spectrum from text file
  return np.genfromtxt(infile) # units: A, 1e-15 erg/s/cm2/A

# Generate blackbody curve
def BB_curve(T=6500, lam_min=4500, lam_max=1e4, N=100): # kelvins and angstroms

  # Constants (cgs units)
  c = 3e10 # cm/s
  h = 6.626e-27 # erg s
  k = 1.38e-16 # erg/K

  lam_step = (lam_max - lam_min)/N # angstroms

  BB = np.zeros((N+1,2))
  for i in range(0, N+1):
    lam = (lam_min + i*lam_step)*1e-8 # cm
    BB[i,0] = lam*1e8
    BB[i,1] = 2*h*c**2/lam**5/(np.exp(h*c/lam/k/T)-1)*1e-8 # erg/s/cm2/A

  return BB

# Reddening function (CCM)
def CCM(lam, A_V=1, R_V=3.1): # angstroms, R_V=A(V)/E(B-V)

  # Wavelength-dependent coefficients (Optical/NIR)
  A = 1e4/lam - 1.82 # inverse microns
  a = 1. + 0.17699*A - 0.50447*A**2 - 0.02427*A**3 + 0.72085*A**4 + 0.01979*A**5 - 0.77530*A**6 + 0.32999*A**7
  b = 1.41338*A + 2.28305*A**2 + 1.07233*A**3 - 5.38434*A**4 - 0.62251*A**5 + 5.30260*A**6 - 2.09002*A**7

  # CCM reddening function (returns A_lambda)
  return A_V*(a + b/R_V)

# Apply reddening to 6500 K blackbody
def red(BB, A_V=1, R_V=3.1): # blackbody, R_V=A(V)/E(B-V)

  BB_red = np.zeros((N+1,2))
  for i in range(0, N+1):
    lam = BB[i,0] # angstroms
    A_lam = CCM(lam, A_V, R_V) # mag
    fac = 10**(-A_lam/2.5) # reduction factor < 1
    BB_red[i,0] = lam
    BB_red[i,1] = BB[i,1]*fac

  return BB_red

# Plot spectra
def red_plot(spec, BB_red): # spectrum, reddened blackbody

  plt.plot(spec[:,0], spec[:,1])
  plt.plot(BB_red[:,0], BB_red[:,1]*spec[910,1]/BB_red[33,1])
  plt.ylim([0, 3])
  plt.show()

# Set variables
infile = '2015-07-24-Berkeley.txt'
T = 6500 # kelvins
low = 4500 # angstroms
high = 1e4 # angstroms
N = 100
A_V = 2 # magnitudes

Berk1 = spec_import(infile)
BB = BB_curve(T=T, lam_min=low, lam_max=high, N=N)
BB_red = red(BB, A_V)
red_plot(Berk1, BB_red)
