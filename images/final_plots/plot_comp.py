#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# Import data
a = np.genfromtxt("phot_data_comp.txt", skip_header=1)

# Extract data from table
ind_J13522 = np.where(a[:,1] != 0)[0]
ind_99em = np.where(a[:,3] != 0)[0]
ind_98S = np.where(a[:,5] != 0)[0]
ind_88Z = np.where(a[:,7] != 0)[0]
ind_87A = np.where(a[:,8] != 0)[0]
ind_10jl = np.where(a[:,9] != 0)[0]
ind_97cy = np.where(a[:,11] != 0)[0]
T_J = a[ind_J13522,0]
M_J = a[ind_J13522,1]
E_J = a[ind_J13522,2]
T_em = a[ind_99em,0]
M_em = a[ind_99em,3]
E_em = a[ind_99em,4]
T_S = a[ind_98S,0]
M_S = a[ind_98S,5]
E_S = a[ind_98S,6]
T_Z = a[ind_88Z,0]
M_Z = a[ind_88Z,7]
T_A = a[ind_87A,0]
M_A = a[ind_87A,8]
T_jl = a[ind_10jl,0]
M_jl = a[ind_10jl,9]
E_jl = a[ind_10jl,10]
T_cy = a[ind_97cy,0]
M_cy = a[ind_97cy,11]

# Define calibrations
# J13522: d = 32.8, A(R) = 1.6
d_J = 32.8
A_J = 1.6
M_J -= (d_J + A_J)
# 99em: d = 33.51, 0=peak and absolute peak = -16.55
d_em = 33.51
peak_em = -16.55
M_em += peak_em
# 98S: d = 31.15
d_S = 31.15
M_S -= d_S
# 88Z: d = 36.4
d_Z = 36.4
M_Z -= d_Z
# 87A: d = 18.55
d_A = 18.55
M_A -= d_A
# 10jl: d = 33.41
d_jl = 33.41
M_jl -= d_jl
# 97cy: d = 37.4
d_cy = 37.4
M_cy -= d_cy

# Plot data with error bars and two y-axes
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax2.errorbar(T_J, M_J, yerr=E_J, fmt='-', color='r')
ax2.errorbar(T_cy, M_cy, fmt='-', color='orange')
ax2.errorbar(T_em, M_em, yerr=E_em, fmt='-', color='y')
ax2.errorbar(T_S, M_S, yerr=E_S, fmt='-', color='g')
ax2.errorbar(T_Z, M_Z, fmt='-', color='c')
ax2.errorbar(T_A, M_A, fmt='-', color='b')
ax2.errorbar(T_jl, M_jl, yerr=E_jl, fmt='-', color='purple')
ax2.plot([250, 350], [-15.5, -14.473955], 'k--')
Mmin, Mmax = ax2.get_ylim()
ax1.set_ylim([Mmin + d_J, Mmax + d_J])
ax2.set_xlim([-10, 450])
ax1.text(200, 15.2, "J13522", color='r')
ax1.text(250, 13.7, "1997cy", color='orange')
ax1.text(150, 19, "1999em", color='y')
ax1.text(160, 17.5, "1998S", color='g')
ax1.text(350, 14.1, "1988Z", color='c')
ax1.text(250, 18.5, "1987A", color='b')
ax1.text(170, 13.3, "2010jl", color='purple')
ax1.text(300, 17.7, r"$^{56}$Co", color='k')
ax1.invert_yaxis()
ax2.invert_yaxis()
ax1.set_xlabel('Days after explosion')
ax1.set_ylabel('Apparent magnitude')
ax2.set_ylabel('Absolute magnitude')
plt.show()

