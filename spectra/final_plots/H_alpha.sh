#!/usr/bin/bash

python <<plot
from plot import specplot
specplot(xmin=-13000, xmax=13000, vel=1, narrow=0, scale='log', shift=3, stretch=0, x_label=-11500, y_label = 0.2, d_label=1)
exit()
plot

