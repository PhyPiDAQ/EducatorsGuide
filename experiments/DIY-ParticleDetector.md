## *PhyPiDAQ*: Recording data from a do-it-yourself particle detector

The detection of radioactivity, either produced by artificial sources or as part of the natural environment
like K-40 or Radon from the inner of the Earth, is a fascinating field of study which today has become
accessible with cheap and simple detectors. There are commercial offers, but also a number of proposals
for do-it-yourself projects. A sound-card of a standard PC is suitable to record the signals, which can then
be visualized with any kind of sound-card oscilloscope. 

*PhyPiDAQ* contains several modules supporting data recording, visualization and analysis. An interesting
and important aspect to study in this context is the randomness of the occurrence of signals. As the probability
to detect a signal is invariant with time, the number of events observed in a given time interval is given by
Poisson statistics. Typical for such a process is the fact that the time between randomly occurring events 
follows an exponential distribution.

The exponential decay of a sample of radioactive nuclei is another important aspect that can be studied if
 a sample of short-lived nuclei can be provided. In Nature, such a source is natural Radon that can be 
 accumulated on an electrically charged balloon. 

Relevant modules of the *PhyPiDAQ* package are:

   - `phypidaq\soundcardOsci` with two classes to record, select  and display waveforms from a PC soundcards

   - `phypidaq/DisplayPoissonEvent`, a class to display a pulse corresponding to a single Poisson event 

Ready-to use scripts  illustrate how to use these classes: 

   - ¸phypidaq/examples/oscilloscope/soundcardOsci.py` to record and display wave forms from a sound card.  

  - *phypidaq/examples/scGammaDetector.py` to visualize every occurrence of a large signal and also the 
  associated wave form data around the trigger point. A rate history is also shown. The script also offers the 
  possibility to store the event times in a file for off-line analysis, or to only visualize a sub-set of triggering
   pulses if the rate is very high. 
   
 Studies of Poisson processes are possible by using scripts
 
  - *phypidaq/examples/poissonFlash* to generate, visualize and store data of a simulated Poisson process. 

  - *phypidaq/examples/poissonLED* produces random flashes of a LED. A photodiode exposed to the light of
     the LED will produce signals analogous to  a detector for gamma rays.


### The CERN DIY particle detector 

A rather recent proposal of a simple, cheap and easy to operate particle detector based on four silicon 
PIN photo-diodes is the [CERN DIY_particle_detector](https://github.com/ozel/DIY_particle_detector). 
The two-stage amplifier with a high-bandwidth op-amp produces large signals of several hundred mV
 shaped to a width of about 100 µs. Such signals can be easily recorded with a standard sound card. 
 
 The availability of necessary parts including the printed circuit board and the large and long signals
 make this detector an ideal choice for projects with high-school students. Besides building the device,
 experience is gained in data acquisition and data analysis of a fascinating phenomenon not directly 
 accessible by human senses. 

### Results of measurements

  to be written ....