#!/usr/bin/env python3
"""RadonAnalysis.py

Count rate as a function of time

uses .csv file provided by scGammaDetector.py and calculates:

- pulse-height distribution
- number of events per time interval (rate)

Parameters:

  - file name
  - number of bis for pulse-height histogram
  - time interval
  - cut on minimal pulse height

"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import argparse


#
# -*- relevante Verteilungen
#
def fUniform(x, const=None):
    """Gleichvderteilung"""
    if hasattr(x, "__iter__"):
        return const * np.ones(len(x))
    else:
        return const


def fExponential(x, tau=None, N=1.0):
    """Exponenitalverteilung"""
    return N / tau * np.exp(-x / tau)


def fPoisson(x, mu=None, N=1.0):
    """Poissonverteilung"""
    k = np.around(x)
    return N * (mu**k) / np.exp(mu) / sp.gamma(k + 1.0)


def getHistDistribution(bc, bw, f, **kwargs):
    """Distribution function f(**kwargs) for bin centres bc and bin widths bw"""
    return bw * f(bc, **kwargs)


print(f"*==* script {sys.argv[0]} executing, parameters: {sys.argv[1:]}\n")

# -*- Eingabe-Parameter
parser = argparse.ArgumentParser(description="Analysis of DIY Detector")
parser.add_argument("inFileName", help="input file name (CSV format)")
parser.add_argument("-b", "--bins", type=int, default=100, help="bins for Pulse Height Histogram (100)")
parser.add_argument("-i", "--interval", type=int, default=60, help="time interval for Rate Histogram (60)")
parser.add_argument("-c", "--cut", type=int, default=0, help="cut on minimal pulse height (0)")
args = parser.parse_args()
inFileName = args.inFileName
NHbins = args.bins
Tinterval = args.interval
phCut = args.cut

# -*- Daten einlesen:
try:
    Traw, H = np.loadtxt(inFileName, skiprows=1, usecols=(1, 2), delimiter=",", unpack=True)
except Exception as e:
    print(" Problem reading input - ", e)
    sys.exit(1)

# Grafiken erzeugen
#  - für Pulshöhen
figH = plt.figure("PulseHeight", figsize=(8.0, 5.0))
ax_ph = figH.add_subplot(1, 1, 1)  # for pulse-height histogram
ax_ph.grid()

# -*- selektiere Daten mit großer Pulshöhe
T = Traw[H > phCut]

# - für Statistik
figS = plt.figure("Rate", figsize=(8.0, 5.0))
figS.subplots_adjust(left=0.12, bottom=0.1, right=0.98, top=0.97, wspace=0.3, hspace=0.25)
ax_rate = figS.add_subplot(1, 1, 1)  # for rate vs. time
mn = 0.0
mx = 75.0
nb = 75  # minimum, maximum and number of bins
N = len(T)
Ttot = T[-1] - T[0]  # total time
NTbins = int(Ttot / Tinterval)  # number of time intervals
meanRate = N / Ttot  # mean rate
meanN = meanRate * Tinterval  # number of events per time interval
dT = T[1:] - T[:-1]  # Zeiten zwischen zwei Ereignissen
meanTw = dT.mean()

# decay times of PB-214 and Bi-214
tauPb = 26.8 / np.log(2)  # Pb-214 lifetime in min
tauBi= 19.9 / np.log(2)  # Bi-214 lifetime in min

# -*-  Ausgabe der statistischen Daten
print(" Intervall: %.3gs" % (Tinterval))
print("   mittlere Rate: %.3g Hz" % (meanRate))
print("   mittlere Zeit zwischen zwei Ereignissen: %.3g s" % (meanTw))
print("\n")

# -*- Erzeugen der Grafiken (als Häufigkeitsverteilungen)

# 1. Pulshöhen
ax_ph.hist(H, NHbins)
ax_ph.set_ylabel(f"Counts")
ax_ph.set_xlabel("Pulshöhe (ACD-counts)")
ax_ph.set_title("peak-to-peak Pulshöhenspektrum")
# set logarithmic scale
ax_ph.set_yscale("log")

# 2. Ereignisse über der Zeit (= Häufigkeit / Zeitinterval)
tmn = 0.0
tmx = NTbins * Tinterval
tbins = np.linspace(tmn/60., tmx/60., NTbins)
bcR, beR, _ = ax_rate.hist(T/60., bins=tbins, ec="grey")
ax_rate.set_ylabel(f"Counts/{Tinterval/60.} min", size="x-large")
ax_rate.set_xlabel("$t$ [min]", size="x-large")
# Mittelpunkt und Breite der Bins
bc = (beR[:-1] + beR[1:]) / 2.0
bw = beR[1] - beR[0]

offset = 16 # time when sensor was exposed to Radon 
#tplt = np.linspace(tmn/60., tmx/60.- offset, NTbins*10 - int(10*offset/Tinterval))
tplt = np.linspace(tmn/60., tmx/60.- offset, NTbins - offset)
N0_0 = 1300
f = 0.0 # initial fraction of Bi
N0 = N0_0 * np.exp(-tplt/tauPb)
dN0 = N0[0:-1] - N0[1:]
#
N1 = np.zeros(len(tplt))
N1[0] = f * N0_0
N1[1:] = dN0
dN1 = np.zeros(len(tplt))
for i, _t in enumerate(tplt[:-1]): 
   dN1[i+1:] = dN1[i+1:] + N1[i] * (np.exp(-tplt[i:-1]/tauBi) - np.exp(-tplt[i+1:]/tauBi))
dN = dN0 + dN1[1:] + 1.3
ax_rate.plot(offset + tplt[:-1], dN * bw)
ax_rate.plot(offset + tplt[:-1], dN0 * bw)
ax_rate.plot(offset + tplt[:-1], dN1[1:] * bw)


# zeichne Gleichverteilung ein
# hDist = getHistDistribution(bc, bw, fUniform, const=meanRate)
# ax_rate.plot(bc, hDist, "g--")

plt.show()
