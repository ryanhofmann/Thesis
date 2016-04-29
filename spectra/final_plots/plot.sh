#!/bin/bash

python <<plot
from plot import specplot
specplot(xmin=0, xmax=0, vel=0, narrow=0, scale='log', shift=1, stretch=0, x_label=5200, y_label = -0.3, d_label=1)
exit()
plot

