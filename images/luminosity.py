#!/usr/bin/python

import numpy as np

# Define function for calculating luminosity from absolute magnitude
def Lum(M):

  # Define absolute magnitude of Sun
  Msun = 4.75

  # Compute luminosity, neglecting bolometric correction
  return 10.**((Msun - M)/2.5)


# Define function for calculating integrated luminosity
def IntL(infile, Mcol=5, skip_header=1):

  # Read in data from table
  data = np.genfromtxt(infile, skip_header=skip_header)
  days = data[:, 0]
  M = data[:, Mcol]
  Me = data[:, Mcol+1]

  # Delete missing data indices
  idx = np.where(M != 0)
  days = days[idx]
  M = M[idx]
  Me = Me[idx]

  # Convert magnitudes to absolute magnitudes
  Dmod = 32.8
  Mabs = M - Dmod

  # Convert to luminosities
  L = np.zeros(len(M))
  Leplus = np.zeros(len(M))
  Leminus = np.zeros(len(M))
  for i in range(0, len(M)):
    L[i] = Lum(Mabs[i])
    Leplus[i] = np.abs(Lum(Mabs[i] + Me[i]) - Lum(Mabs[i]))
    Leminus[i] = np.abs(Lum(Mabs[i]) - Lum(Mabs[i] - Me[i]))

  # Integrate with trapezoid rule (approximate)
  Lsun = 3.828e33 # Solar luminosity in erg/s
  E = 0 # Total emitted energy
  Eeplus = 0
  Eeminus = 0
  for i in range(1, len(L)):

    # Compute energy emitted at Lmean over dt
    Lmean = 0.5*(L[i] + L[i-1])
    dt = (days[i] - days[i-1])*86400
    E += Lmean*Lsun*dt

    # Compute errors
    Leplusmean = 0.5*(Leplus[i] + Leplus[i-1])
    Leminusmean = 0.5*(Leminus[i] + Leminus[i-1])
    Eeplus += Leplusmean*Lsun*dt
    Eeminus += Leminusmean*Lsun*dt

  # Return total energy and errors
  return E, Eeplus, Eeminus


if __name__ == '__main__':

  import sys

  # Get inputs
  infile = sys.argv[1]

  # Compute total energy
  E, Eeplus, Eeminus = IntL(infile)

  # Print results
  exp = np.log10(E) - np.log10(E) % 1
  Ebase = E/10**exp
  Eeplusbase = Eeplus/10**exp
  Eeminusbase = Eeminus/10**exp
  print "Total emitted energy: [%.3f +%.3f/-%.3f]e%2d erg" % (Ebase, Eeplusbase, Eeminusbase, exp)
