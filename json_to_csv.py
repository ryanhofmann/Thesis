#!/usr/bin/python

import sys

# Extract photometry from json in specific band
if len(sys.argv) != 4:
  print "Usage: json_to_csv json csv band"
  exit(0)

json = sys.argv[1]
csv = sys.argv[2]
band = sys.argv[3]

time = []
mag = []

# Read through json to photometry section
with open(json) as f:
  for line in f:
    if "photometry" in line:
      break
  # Extract photometry in specified band
  t, b, m = "", 0, ""
  for line in f:
    if "spectra" in line:
      break
    if "\"time\"" in line:
      t = line.split("\"")[-2]
      continue
    if "band" in line:
      if band in line:
        b = 1
        continue
      else:
        t = ""
        continue
    if "\"mag" in line and t != "" and b == 1:
      m = line.split("\"")[-2]
      time.append(t)
      mag.append(m)
      t, b, m = "", 0, ""

# Write photometry to text file
with open(csv, 'w') as f:
  for i in range(0, len(time)):
    f.write("%s,%s\n" % (time[i], mag[i]))
