#!/bin/bash

python <<plot
from plot import specplot
specplot(xmin=4000, xmax=10000, vel=0, narrow=0, scale='log', shift=4, stretch=0, x_label=5150, y_label = -0.3, d_label=1)
exit()
plot

