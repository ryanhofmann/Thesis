#!/bin/bash

python << plot
import plot
plot.plot('phot_data.txt', multi=0)
plot
