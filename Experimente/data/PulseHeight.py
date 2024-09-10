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

# -*- coding=utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt

# -*- Eingabe-Parameter

print(f"*==* script {sys.argv[0]} executing, parameters: {sys.argv[1:]}\n")

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = "pFilt.dat"  #  input file

if len(sys.argv) > 2:
    Nbins = int(sys.argv[2])
else:
    Nbins = 100  #  number of bins

fig = plt.figure(1, figsize=(6.0, 4.0))
ax = fig.add_subplot(1, 1, 1)  # for rate vs. time

# -*- Daten einlesen:
try:
    H = np.loadtxt(fname, skiprows=1, usecols=(2), delimiter=",", unpack=True)
except Exception as e:
    print(" no input file given - abort")
    sys.exit(1)

ax.hist(H, Nbins)
ax.set_ylabel("Anzahl Einträge")
ax.set_xlabel("Pulshöhe (ACD-counts)")
ax.set_title("Pulshöhenspektrum")

plt.show()
