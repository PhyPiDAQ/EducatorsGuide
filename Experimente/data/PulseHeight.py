#!/usr/bin/env python3
"""PulseHeight.py

pulse height histogram

uses .csv file provided by scGammaDetector.py and calculates:

- number of events per time interval (rate)
- distribution of rates (Poisson)
- distribution of time between events (exponential)

Parameters:

  - file name
  - number of bins
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

# -*- input parameters

print(f"*==* script {sys.argv[0]} executing, parameters: {sys.argv[1:]}\n")

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = "pFilt.dat"  #  input file

if len(sys.argv) > 2:
    Nbins = int(sys.argv[2])
else:
    Nbins = 100  #  number of bins

# -*- read data

try:
    ph_data = np.loadtxt(fname, skiprows=1, usecols=(2), delimiter=",", unpack=True)
except Exception as e:
    print(" no input file given - abort")
    sys.exit(1)

# -*- create figure a show histogram

fig = plt.figure(1, figsize=(8.0, 5.0))
ax = fig.add_subplot(1, 1, 1)  # for pulse-height histogram

ax.hist(ph_data, Nbins)
ax.set_ylabel("Anzahl Einträge")
ax.set_xlabel("Pulshöhe (ACD-counts)")
ax.set_title("peak-to-peak Pulshöhenspektrum")

plt.show()
