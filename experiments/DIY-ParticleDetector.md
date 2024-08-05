## *PhyPiDAQ*: Recording data from a do-it-yourself particle detector

The detection of radioactivity, either produced by artificial sources or as part of the natural environment
like K-40 or Radon from the inner of the Earth, is a fascinating field of study which today has become
accessible with cheap and simple detectors. There are commercial offers, but also a number of proposals
for do-it-yourself projects. A sound-card of a standard PC is suitable to record the signals, which can then
be visualized with any kind of sound-card oscilloscope. 

### The CERN DIY particle detector 

A rather recent proposal of a simple, cheap and easy to operate particle detector based on four silicon 
PIN photo-diodes(BPW34)  is the [CERN DIY_particle_detector](https://github.com/ozel/DIY_particle_detector). 
A two-stage amplifier with a high-bandwidth op-amp produces large signals of several hundred mV
shaped to a width of about 100 µs. Such signals can be easily recorded with a standard sound card. 
 
 The commercial availability of all necessary parts including the printed circuit board and the large and 
 long output signals make this detector an ideal choice for projects with high-school students. Besides 
 building the device, additional experience is gained in data acquisition software and data analysis of a
 fascinating phenomenon not directly accessible by the human senses. 

### Signal recording and analysis with *PhyPiDAQ*

*PhyPiDAQ* contains several modules supporting data recording, visualization and analysis. An interesting
and important aspect to study in this context is the randomness of the occurrence of signals. As the probability
to detect a signal is invariant with time, the number of events observed in a time interval is given by
Poisson statistics. Typical for such a process is the fact that the time between randomly occurring events 
follows an exponential distribution.

In addition, the exponentially falling decay rate of a sample of radioactive nuclei is another important aspect 
that can be studied if a sample of short-lived nuclei can be provided. In Nature, such a source is Radon produced 
from radioactive decays in the inner of the earth; decay products of Radon, which are themselves radioactive, 
can be  accumulated on an the surface of an electrically charged balloon. 

Relevant modules of the *PhyPiDAQ* package are:

   - `phypidaq\soundcardOsci` with two classes to record and select  and to display waveforms from a PC soundcard

   - `phypidaq/DisplayPoissonEvent`, a class to display a pulse corresponding to a single Poisson event and to show 
   a rate history. 

Ready-to use scripts  illustrate how to use these classes: 

   - `examples/oscilloscope/soundcardOsci.py` to record and display wave forms from a sound card.  

  - `examples/scGammaDetector.py` to visualize every occurrence of a large signal and also the 
  associated wave form data around the trigger point. A rate history is also shown. The script also offers the 
  possibility to store the event times in a file for off-line analysis, or to only visualize a sub-set of triggering
   pulses if the rate is very high. 
   
 Studies of Poisson processes are possible by using scripts
 
  -  `examples/poissonFlash.py` to generate, visualize and store data of a simulated Poisson process, and  

  - `examples/poissonLED.py` to produce random flashes of a LED. A photodiode exposed to the light of
     the LED will produce signals analogous to  a detector for gamma rays.

 A typical waveform recorded after issuing the command *scGammaDetector.py -o* on the command line 
 is shown in the figure below. The signal is clearly visible above the noise level of approx. 3500 ADC counts. 
 It  is sufficiently large to be directly connected to a earphone so that the signal clicks can also be acoustically 
 perceived. 
 
 ![Fig. 1: Typical waveform recorded with a LogiLink USB soundcard with 16 bit resolution and a sampling rate
 of 96000/s is shown below. Note that the y-axis only shows a range of +/- 2¹⁴](images/scOscillogram.png)

The script provides a number of command line options to control the visual output, enable storage of results to a file,
and to set up the parameters of the soundcard and the trigger options. 

The output of the command `./scGammaDetector -h` is shown here: 

```
usage: scGammaDetector.py [-h] [-q] [-o] [-n] [-f FILE] [-t TIME] [-s {48000,96000,192000,44100}] [-c {1,2}]
                          [-l TRGLEVEL] [--trgfalling] [-d] [-z SAMPLESIZE] [-r RANGE] [-i INTERVAL]

Read waveforms from soundcard and display and optionally store data

options:
  -h, --help            show this help message and exit
  -q, --quiet           no status output to terminal
  -o, --oscilloscope    oscilloscope display
  -n, --noeventdisplay  deactivate event display
  -f FILE, --file FILE  base filename to store results
  -t TIME, --time TIME  run time in seconds
  -s {48000,96000,192000,44100}, --samplingrate {48000,96000,192000,44100}
                        sampling rate
  -c {1,2}, --channels {1,2}
                        number of channels
  -l TRGLEVEL, --trglevel TRGLEVEL
                        level of trigger
  --trgfalling          trigger falling edge
  -d, --trgdeactivate   deactivate triggering
  -z SAMPLESIZE, --samplesize SAMPLESIZE
                        number of samples per read
  -r RANGE, --range RANGE
                        display range
  -i INTERVAL, --interval INTERVAL
                        time bin for rate display
```

Reasonable default settings are available so that in most cases useful output is generated. Because the signal rate is  
very low in normal environments without a radioactive source, the trigger level should be set to be just above noise  
level so that some noise pulses become visible. It is also advisable to use the option `-o` to switch on the oscilloscope view. 
Note that the signal level depends on the  settings of the soundcard. Use the appropriate tool of your PC operating system to 
select the standard input device used for sound recording and adjust the volume control. 

The output shown under measurement conditions at low rates is shown in the figure below. A flashing circle indicates  
the occurrence of triggered event, and the corresponding (normalized) wave form with 100 sampling points around
the trigger time is displayed. A rate history is also shown; the bin width in seconds can be set using the opton `--interval <n>` 

![Fig. 2: Graphical display showing data acquisition with a small sample of pitchblende ore.
 An average count rate of about 5 signals in 5 s intervals is observed.](images/PoissonEventDisplay.png)



### Results of measurements

  to be written ....