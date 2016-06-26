#!/bin/bash

python << plot
import plot
plot.plot('phot_data_rev.txt', multi=1)
plot
