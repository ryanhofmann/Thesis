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
e_mag = []
mag = []

# Read through json to photometry section
with open(json) as f:
  for line in f:
    if "photometry" in line:
      break
  # Extract photometry in specified band
  t, b, m, e = "", 0, "", ""
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
    if "\"e_mag" in line and t != "" and b == 1:
      e = line.split("\"")[-2]
      e_mag.append(e)
    if "\"mag" in line and t != "" and b == 1:
      m = line.split("\"")[-2]
      time.append(t)
      mag.append(m)
      t, b, m, e = "", 0, "", ""

# Write photometry to text file
with open(csv, 'w') as f:
  for i in range(0, len(time)):
    if len(e_mag) != 0:
      f.write("%s,%s,%s\n" % (time[i], mag[i], e_mag[i]))
    else:
      f.write("%s,%s\n" % (time[i], mag[i]))
