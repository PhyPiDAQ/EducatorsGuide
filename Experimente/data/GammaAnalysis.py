#!/usr/bin/env python3
"""GammaAnalysis.py

statistical analysis of arrival times of random events

uses .csv file provided by scGammaDetector.py and calculates:

- pulse-height distribution
- number of events per time interval (rate)
- distribution of rates (Poisson)
- distribution of time between events (exponential)

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
parser.add_argument(
    "-b", "--bins", type=int, default=100, help="bins for Pulse Height Histogram (100)"
)
parser.add_argument(
    "-i",
    "--interval",
    type=int,
    default=30,
    help="time interval for Rate Histogram (30)",
)
parser.add_argument(
    "-c", "--cut", type=int, default=0, help="cut on minimal pulse height (0)"
)
args = parser.parse_args()
inFileName = args.inFileName
NHbins = args.bins
Tinterval = args.interval
phCut = args.cut


# -*- Daten einlesen:
try:
    Traw = np.loadtxt(inFileName, skiprows=1, usecols=(1), delimiter=",", unpack=True)
    H = np.loadtxt(inFileName, skiprows=1, usecols=(2), delimiter=",", unpack=True)
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
figS = plt.figure("Statistics", figsize=(6.0, 11.0))
figS.subplots_adjust(
    left=0.12, bottom=0.1, right=0.98, top=0.97, wspace=0.3, hspace=0.25
)
ax_rate = figS.add_subplot(3, 1, 1)  # for rate vs. time
ax_rdist = figS.add_subplot(3, 1, 2)  # for distribution of rates
ax_tw = figS.add_subplot(3, 1, 3)  # for wait-time
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

# -*-  Ausgabe der statistischen Daten
print(" Intervall: %.3gs" % (Tinterval))
print("   mittlere Rate: %.3g Hz" % (meanRate))
print("   mittlere Zeit zwischen zwei Ereignissen: %.3g s" % (meanTw))
print("\n")

# -*- Erzeugen der Grafiken (als Häufigkeitsverteilungen)

# 1. Pulshöhen
ax_ph.hist(H, NHbins)
ax_ph.set_ylabel("Anzahl Einträge")
ax_ph.set_xlabel("Pulshöhe (ACD-counts)")
ax_ph.set_title("peak-to-peak Pulshöhenspektrum")
# set logarithmic scale
ax_ph.set_yscale("log")

# 2. Ereignisse über der Zeit (= Häufigkeit / Zeitinterval)
tmn = 0.0
tmx = NTbins * Tinterval
bcR, beR, _ = ax_rate.hist(T, bins=np.linspace(tmn, tmx, NTbins))
ax_rate.set_ylabel("Anzahl Einträge", size="x-large")
ax_rate.set_xlabel("$t$ [s]", size="x-large")
# Mittelpunkt und Breite der Bins
bc = (beR[:-1] + beR[1:]) / 2.0
bw = beR[1] - beR[0]
# zeichne Gleichverteilung ein
hDist = getHistDistribution(bc, bw, fUniform, const=meanRate)
ax_rate.plot(bc, hDist, "g--")

# 3. Verteilung der Anzahlen n beobachteter Ereignisse pro Zeitintervall
#      Bereich festlegen
meanEntries = int(meanRate * Tinterval)
nBins = max(5 * np.sqrt(meanEntries), 5)
mn = max(meanEntries - nBins, 0)
mx = meanEntries + nBins
bins = np.arange(mn, mx, 1)
#      Verteilung als schmale Balken
bcP, beP, _ = ax_rdist.hist(bcR, bins, align="left", rwidth=0.3)
ax_rdist.set_ylabel("Anzahl Einträge", size="x-large")
ax_rdist.set_xlabel("$n$", size="x-large")
# Mittelpunkt und Breite der Bins
bc = (bins[:-1] + bins[1:]) / 2.0
bw = bins[1] - bins[0]
# zeichne Poisssonverteilung ein
hDist = getHistDistribution(bins[:-1], bw, fPoisson, mu=meanN, N=len(beR) - 1)
ax_rdist.plot(bins[:-1], hDist, "g--")

# 4. Wartezeiten
mn = 0.0
mx = 5 * meanTw
nb = 75  # minimum, maximum and number of bins
bcW, beW, _ = ax_tw.hist(
    dT, bins=np.linspace(mn, mx, nb), log=True, rwidth=0.8
)  # log. Darstellung
ax_tw.set_ylabel("Anzahl Einträge", size="x-large")
ax_tw.set_xlabel("$\Delta$t [s]", size="x-large")
# Mittelpunkt und Breite der Bins
bc = (beW[:-1] + beW[1:]) / 2.0
bw = beW[1] - beW[0]
# zeichne Gleichverteilung ein
hDist = getHistDistribution(bc, bw, fExponential, tau=1.0 / meanRate, N=N)
ax_tw.plot(bc, hDist, "g--")

# Grafiken anzeigen
plt.show()
