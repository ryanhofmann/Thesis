#!/bin/bash

python <<plot
from plot import specplot
specplot(xmin=5700, xmax=6100, vel=0, narrow=1, scale='log', shift=3, stretch=0, x_label=6070, y_label = 0.1, d_label=1)
exit()
plot

