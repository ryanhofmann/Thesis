#!/bin/bash

python <<plot
from plot import specplot
specplot(xmin=-1000, xmax=1000, vel=1, narrow=1, scale='lin', shift=3, stretch=0, x_label=-900, y_label = 0.2, d_label=1.6)
exit()
plot

