# PhyPiDAQ documentation (for teachers)

---  

This is the English version for educators of the project PhyPiDAQ, 
a package for acquisition, storage, visualization and analysis of measurement data 
with the [Raspberry Pi](https://www.raspberrypi.com/).

Hier gibt es die [Deutsche Version](Dokumentation_de.md).  

---  

In this document, the entire PhyPiDAQ workflow, starting from the  
Installation up to descripotions of concrete experiments is described.  

- [What is PhyPiDAQ?](#wasistphypidaq)
- [What do I need and how do I assemble it?](#wasbraucheichundwiebaueichdaszusammen)
- [How do I set up the Raspberry Pi and install PyPiDAQ?](#wiesetzeichdenraspberrypiaufundinstalliereichphypidaq)
    - [How do I set up the Raspberry Pi?](#wiesetzeichdenraspberrypiauf)
    - [How do I install PhyPiDAQ?](#wieinstalliereichphypidaq)
- [How do I use the PhyPiDAQ software?](#wiebedieneichdiephypidaqsoftware)
    - [Starting surface](#startenundstartoberflaeche)
    - [configuration file](#konfigurationsdatei)
    - [starting the measurement](#messungstarten)
- [Experiments with PhyPiDAQ?](#wiefuehreichdamitversuchedurch)  
     - [electrostatics](#elektrostatik)
     - [force sensor](#kraftsensor)
     - [photo effect](#photoeffekt)

&nbps;&nbsp;<a name="wasistphypidaq"> </a>
## 1. What is PhyPiDAQ?

PhyPiDAQ is a project for transparent, easily understandable Data AQuisition (DAQ) 
with a Raspberry Pi. The software contains basic functions for data acquisition and
visualization such as data logger, bar graph, XY or oscilloscope display and data 
recording on disk for subsequent evaluation.

The user interface is designed in such a way that pre-made templates for many 
sensors can be used to read them out quickly and easily.  In addition, it also offers 
the option of changing parameters like, e. g.  sampling rate, range,  axis labeling, 
function evaluation for direct conversion of raw measurements of special sensor
settings. The settings can be conveniently saved and recalled so that initial examples
for own experiments or for a quick demonstration can be easily provided. 

A large number of sensors, such as various analog-digital converters,  current sensors, 
environmental data sensors, gamma ray detectors or a usb-oscilloscope, are supported.
Here, widespread and inexpensive sensors were used, which have a sufficient level
 of accuracy that is more than sufficient for school experiments.  

The sensors can be individually connected to the Raspberry Pi using jumper cables, 
or via a printed board specially designed for use with the PhyPiDAQ software on which
some sensors and amplifiers are permanently attached. The latter set-up reduces
cabling efforts to a minimum and experiments can be set up quickly.  A 3d printed
connection panel and a printed circuit-board  are available so that all components
can be conveniently  provided  in an organizer case.  

*Fig. 1*:  Representation of the time dependence of two signal sources 
(square wave and capacitor voltage) connected to an AD converter  
                    ![Figure 1](images/Kondensator.png)  

*Fig. 2*:  Measurement case with Raspberry Pi, circuit board and built-in display  
                    ![Figure 2](images/Overview_koffer.png)  

&nbsp;  
&nbsp;  
<a name="wasbraucheichundwiebaueichdaszusammen"></a>
## 2. What do I need and how do I assemble it?

Sensors and standard amplifiers are at the heart of the PhyPiDAQ project. 
A number of analog and digital sensors are supported by the PhyPiDAQ software,
which is open source and can be downloaded from the 
[Github repository](https://github.com/PhyPiDAQ/PhyPiDAQ). 
The detailed installation procedure is  described [here](#wiesetzeichdenraspberrypiauf).

Sensors can be directly conneted to the GPIO pins of your Raspberry Pi, and an 
external breadboard may be used to provide amplification of weak signals, if
necessary. 

A proposal for a case containing some of the most common sensors to measure voltages
and currents and a set of standard amplifiers is proposed as part of the PhyPiDAQ
project. Detailed building instructions and a liste of recommended compontents
are described in the folder *MeasuringCase*, which you can also find on the
[Github repository](https://github.com/PhyPiDAQ/MeasuringCase).  


&nbsp;  
&nbsp;  
<a name="wiesetzeichdenraspberrypiaufundinstalliereichphypidaq"></a>  
## 3. How do I set up the Raspberry Pi and install PhyPiDAQ?

If there already is an operating system on the Raspberry Pi, you can  continue directly with 
[3.2](#wieinstalliereichphypidaq). 
If not, proceed with this description how to install the operating system. 

<a name="wiesetzeichdenraspberrypiauf"></a>  
### 3.1 How do I set up the Raspberry Pi?

First download *Raspberry Pi Imager* from the official website  
https://www.raspberrypi.org/downloads/ to any computer with an SD card slot.  

Install the *Raspberry Pi Imager* by double-clicking the downloaded file.  

*Fig. 3*: Installation of Raspberry Pi Imager, double click on the "Raspberry"  
                    ![Figure 3](images/installieren_1.png) 
 
A new window opens in which you can select the operating system to be 
installed and the SD card. Under *Operating System* select "Raspberry 
Pi OS (other)" and then "Raspberry Pi OS Full".

*Fig. 4*: Selection of the operating system  
                    ![Figure 4](images/installieren_2.png)  

*Fig. 5*: Selection of the operating system  
                    ![Figure 5](images/installieren_3.png)  

Insert the SD card into the slot of the computer. Ensure that the SD  card is in writable 
mode by pushing the small slide on the left edge of the  SD card adapter upwards.  

*Fig. 6*: Make the SD card writable, move the slider to the top position  
                    ![Figure 5](images/installieren_4.png)  

In the *Raspberry Pi Imager* you can now select your SD card by clicking on *"SD Card"*.

*Fig. 7*: Selection of the SD card  
                    ![Figure 6](images/installieren_5.png)  

By clicking on *"Write"* and then confirming, you can finally record onto 
the SD card; you may be asked for the password once. This process can now 
take a few minutes.  

*Fig. 8*: Writing to the SD card  
                  ![Figure 8](images/installieren_6.png)  

When the process is complete, the operating system for the Raspberry Pi is 
on the SD card and this can be plugged into the Raspberry Pi. If you have 
not decided to use the case version with a display, connect an external monitor 
and make sure that a mouse and keyboard are connected. Also connect an 
Ethernet cable if you don't have a WiFi connection available. Then you can 
connect the Raspberry Pi to the power supply, and it boots automatically. 
Various packages are now installed automatically, which can take  several minutes. 
If this is successful, a window opens in which you can set  basic system settings such 
as time zone, country, keyboard layout and your  WiFi network, if this is desired. 
The installation of the Pi is now   complete and we can continue installing *PhyPiDAQ*.  


<a name="wieinstalliereichphypidaq"></a>  
### 3.2 Installation of PhyPiDAQ on the Raspberry Pi

**Obtaining the PhyPiDAQ code and easy installation**

Please note that your Raspberry Pi must be connected to the Internet for  
the following steps. Open the terminal, which you can find in the system  
bar at  the top left.  

*Fig. 9*: Open the terminal  
                    ![Figure 9](images/installieren_7.png)  

First install the repository manager *git*, which is used to download all
files of the *PhyPiDAQ* package from its github repository. 
To do this, enter the following texxt in the terminal window:  
`` bash
sudo apt-get install git
``

*Fig. 10*: Enter command in the terminal  
                    ![Figure 10](images/terminal.png)  

Enter the following commands to install *PhyPiDAQ*. Always copy this code 
line by line into the terminal and confirm each command with the Enter key.  
**DO NOT** insert all lines at once.
```bash
mkdir ~/git
cd ~/git
git clone https://github.com/GuenterQuast/PhyPiDAQ
cd ~/git/PhyPiDAQ
./installlibs.sh
cp ~/git/PhyPiDAQ/phypi.desktop ~/Desktop/
```
The installation is now complete and *PhyPiDAQ* is ready for the first use. 
If you want to update the installed version later, enter the following in 
the terminal (not necessary for the first installation, as the current 
version has already been downloaded):  
```bash
cd ~/git/PhyPiDAQ
git pull
./installlibs.sh
```

&nbsp;  
&nbsp;  
<a name="wiebedieneichdiephypidaqsoftware"></a>  
## 4. How do I use the PhyPiDAQ software?<a name="startenundstartoberflaeche"></a>
## 4.1 Start-up interface

To start the *PhyPiDAQ* application, double-click the icon on the desktop **PhyPi**.  

*Fig. 11*: Open PhyPiDAQ  
                    ![Figure 11](images/bedienung_1.png)  

You will be asked how you would like to open it, select "*Run*" here. Two 
windows open now: a black terminal window, which shows current status 
messages and log files. You can ignore this window for ease of use. It only 
gets important when errors are displayed. In this case, the terminal 
window shows the error code and instructions which point to the problem and 
which can usually be used to fix the problem quickly. The more important 
window is the user interface of *PhyPiDAQ*.


*Fig. 12*: User interface *PhyPiDAQ*  
                    ![Figure 12](images/bedienung_2.png)  

The tab "*Control"*, in which you are after opening, is the start tab. A 
measurement can be started from here by clicking the button "*StartRun*" 
at the bottom right, but this should only be tried later. The so-called 
working directory can also be selected in this tab. Here you can determine 
where the configured experiment should be saved. A clear folder structure 
is essential if *PhyPiDAQ* is used in several school classes. So it is 
highly recommended to use a structure like the following:  

*Fig. 13*: folder structure  
                    ![Figure 13](images/ordnerschema.png)  
                    
You can create new folders in the file manager (similar to Windows "My 
Computer" or Mac "Finder") by right-clicking on *"New"* -> *"Folder"* 
in the window.  

*Fig. 15*: create a new folder  
                    ![Figure 15](images/bedienung_3.png)  

Another possibility is to enter the following command in the terminal, 
which creates the subfolder *"class_12"* in the folder *"school"*.  
```bash
mkdir /home/pi/PhyPi/school/class_12
```
In the PhyPiDAQ user interface you select in the field *"Work Dir:"* in 
which folder you want to save the current project. Below that, in *"DAQ 
config*", you can open projects that have already been saved. This is 
particularly useful if you have already tested an experiment in advance and 
want to demonstrate it in class. The saved project will then be opened 
again in exactly the same way and you can start the experiment immediately. 
Below, in the field *"Name"* you can enter the name of the experiment. 
This will appear in the file name. If you click on *"Save Config"*, you 
save the configuration file. The file will then be called "default.daq" if 
you wrote "default" in *Name:*. Each time you start the program with 
"StartRun", an additional file is created with name, time and date, which 
is saved in the directory you specified for "Work Dir", 
e.g. school/class_12/photoeffect.

**Task:** Now create a folder structure as shown in Fig. 30 with your 
school classes. Create a folder with the name *"Test"* in one of these 
classes. Then switch to the *PhyPiDAQ* user interface and select the 
*test* you just created in *Work Dir*. Now assign the name 
"standard experiment" and save the project. Then verify in the file 
manager that the created project is there.


<a name="konfigurationsdatei"></a>
## 4.2 configuration file

We now want to familiarize ourselves with the second tab, *"Configuration"*. 
Click on the tab *"Configuration"*.  

*Fig. 16*: configuration  
                    ![Figure 16](images/bedienung_4.png)  
A window can now be seen in which all parameters for the experiment can be 
set, such as:

  - which sensor do I use (DeviceFile)?  
  - which maximum values ​​should be displayed in the diagram (ChanLimits)?  
  - should the values ​​of the sensor be converted directly (ChanFormula)?  
  - which axis labeling should be displayed (ChanLabels)?  
  - which formulas should be displayed (ChanUnits)?  
  - how often should be scanned (Interval)?  

and many more...

Don't let this put you off! These parameters represent ways in which an 
experiment can be expanded or perfected. By no means all parameters are 
required - usually around 3-5 lines are sufficient. In the *"default"* - 
Config, which can be seen in Fig. 32, all setting options are 
indicated  and can be commented out by a "#" at the beginning of the 
respective line.

If you want to make changes to this configuration, you must first activate 
the *"Edit Mode"* at the top right by clicking on it once. 
The field in front of it shows that you can now write into the text field. 
Helpful Keyboard shortcuts are:

  - *Str + C* for copying selected characters
  - *Str + V* for pasting the characters you just copied
  - *Str + Z* for undo
  - *Str + Shift + Z* to undo again.

Always start by telling the software which sensor you want to read out by 
removing the "#" at the beginning of the corresponding line.  

We now want to read out the ADS1115 analog-to-digital converter 
demonstratively and therefore change the line  
```bash
#DeviceFile: config/ADS1115Config.yaml   # 16 bit ADC, I2C bus
```
to
```bash
DeviceFile: config/ADS1115Config.yaml   # 16 bit ADC, I2C bus
```
You can leave all other settings here unchanged, as suitable parameters for this  
sensor are automatically selected. Changes may have to be made to the sensor,  
because e.g. it has four inputs but not all of them have to be  
read out depending on the project. To do this, click on *"reload device config"*,  
which you will find at the bottom right. A confirmation follows that *PhyPiDAQ*  
has now accepted the selected sensor.

<a name="sensorkonfiguration"></a>
### 4.2.1 Sensor configuration "Device-Config"

Now click on the tab *"Device Config"* at the top. The parameters of the sensor can be seen now.

*Fig. 17*: Configuration of the sensor  
                    ![Figure 17](images/bedienung_5.png)  

Here the syntax is the same again, that means:

  - Lines that begin with "#" are commented out and have no function on the program
  - To make changes you have to go to "Edit-Mode" by clicking above on the 
    "Edit-Mode" field on the right.

You now have the choice of which channels you want to read out, as determined 
in "ADCChannels". If you only want to read out channel 1, this is  the line: 
```bash
ADCChannels: [0]
```
because counting starts at zero. If you only want to read out channel 2, this 
is the line:
```bash
ADCChannels: [1]
```
You can read out several inputs at the same time by separating the individual 
channels with commas:
```bash
ADCChannels: [0, 1, 2, 3]
```
The other parameters below can be used if necessary, for example to subtract one 
input from another. To do this, follow the instructions in the corresponding 
lines. Please note that if you want to read out several channels, you also have 
to adjust the parameters below to the respective number of channels. So the 
following is not possible and will lead to an error message:
```bash
# example of a configuration file for ADC ADS1115

DAQModule: ADS1115Config  

ADCChannels: [0, 1, 2, 3]         # active ADC-Channels
DifModeChan: [false]   # enable differential mode for Channels
Gain: [2/3]                # programmable gain of ADC-Channel
sampleRate: 860             # programmable Sample Rate of ADS1115
```
Correct is:
```bash
# example of a configuration file for ADC ADS1115

DAQModule: ADS1115Config  

ADCChannels: [0, 1, 2, 3]         # active ADC-Channels
DifModeChan: [false, false, false, false]   # enable differential mode for Channels
Gain: [2/3, 2/3, 2/3, 2/3]                # programmable gain of ADC-Channel
sampleRate: 860             # programmable Sample Rate of ADS1115
```

We have now selected the sensor *ADS1115* with four channels. You can now assign 
a name below and save the configuration.

Now connect the analog-digital converter to the Raspberry Pi - four wires are required:  
GND and + 5V for the power supply and SCL and SDA for the *i2C* connection for the data 
transmission from the sensor to the Pi.

<a name="messungstarten"></a>
## 4.3 Starting the measurement

Then you can click the button *"StartRun"*. A window with the diagram opens and
you can start the measurement by clicking at the bottom left on *"Run"*.
Congratulations, you have taken your first measurement with *PhyPiDAQ*! 
Fig. 18 shows the graphical display you should see.

*Fig. 18*: Reading out four channels with an analog-digital converter  
                    ![Figure 18](images/bedienung_6.png)  


There are numerous ways in which you can interact wiht *PhyPiDAQ*. On the one hand, it 
is important to be able to save recorded data, which is done with the button *"SaveData"*. 
The values are saved in the folder selected in the working directory (*"WorkDir"*) in the 
folder belonging to the measurement. By default, only the first 12 seconds are saved, which 
is exactly the interval that can be seen in the display. In the configuration this can of 
course be adjusted and extended if desired. The standard data format is *".csv"*, which can 
also be adapted.

Keyboard shortcuts are defined for all buttons, as indicated by the '_' on the
button text. In many practical cases, typing a button is much easier than interacting via the mouse.


&nbsp;  
&nbsp;  
<a name="wiefuehreichdamitversuchedurch"></a>  
## 5. Experiments with *PhyPiDAQ*

We are now ready to read out a large number of different sensors, graphically 
plot them live on the monitor and export the values. That opens up countless 
possibilities to use *PhyPiDAQ* in the classroom. 

There is an introductory Course in German languge, 
[Kurs digitale Messswerterfassung](
docs/Kurs_digitale_Messwerterfassung_mit_PhyPiDAQ.md), which has not yet been
translated to English. 
Starting with very basic material on digitization and data processing with *Python*, 
a first project deals with a non-linear, temperature dependent resistor, an NTC, 
which is first calibrated and then used in a self-made thermometer. 
As a  more advanced example involving active amplification of a weak signal, a load-cell 
as contained in standard kitchen scales is used to build a very sensitive force sensor. 

Some more advanced sample experiments from different areas of Phyics are described below 
to illustrate the entire *PhyPiDAQ* workflow from start to end.

&nbsp;<a name="elektrostatik"></a>
### 5.1 Electrostatics

In the following experiment, the effect of electrostatic influence will be shown. 
Furthermore, the same setup can also be used to demonstrate a load spoon.  

An open, round capacitor plate with a diameter of d ≈ 5 cm is connected to the 
electrometer. The mass of the measuring case is pulled to the earth potential. 
A capacitor with a capacity of 1 nF is connected between the capacitor plate 
and the earth. The output of the electrometer is connected to the level converter 
and this in turn to the ADC. This means that both positive and negative 
voltages can be read out.

**elektrostatik.daq:**
*Fig. 19*: Electrostatic experiment setup  
                    ![Figure 19](images/elektrostatik_1.png)  

We now deal with the configuration file. For the sake of clarity, superfluous comments and 
lines that have been commented out have been left out.
```bash
DeviceFile: config/myADS1115Config.yaml   # 16 bit ADC, I2C bus 
ChanLabels: ['Uc']            # names for channels 
ChanUnits: ['V']         # units for channels 
ChanColors: [darkblue]      # channel colours in display
ChanFormula:
  - 2*c0-5  # chan0
Interval: 0.1                 # logging interval 
DisplayModule: DataGraphs     # text, bar-graph, history and xy-view
Title: "Data from File"       # display title
```
**myADS1115Config.yaml:** 
```bash  
# example of a configuration file for ADC ADS1115

DAQModule: ADS1115Config  

ADCChannels: [0]         # active ADC-Channels
DifModeChan: [false]   # enable differential mode for Channels
Gain: [1]                # programmable gain of ADC-Channel
sampleRate: 860             # programmable Sample Rate of ADS1115  
```
You may have to adjust the *Gain* in the penultimate line - depending on whether 
the displayed signal is too small or too large. On the software side, the function 
of the level converter is compensated as follows:  
U<sub>capacitor</sub> = 2 · U<sub>measured</sub>-5V, which is already taken 
into account in *ChanFormula*.  
Before the measurement begins, the capacitor plate is connected to earth potential 
using a conductor so that it is uncharged. If a charged body is brought closer to the capacitor plate, the electric 
field of the charged body causes a force on the free electrons of the capacitor plate, which then - depending on the 
body's charge - are accelerated towards or away from it (electrostatic influence). This process is limited by the fact 
that an 
electric field is built up through the charge shift, which counteracts the accelerating force.
  
The charge separation can be measured as an electrical voltage between earth and the capacitor plate, i.e. precisely on 
the input side of the electrometer. It 
should be noted that an electrometer with a very high internal resistance is 
absolutely necessary for this experiment, as otherwise current flow 
between the input of the electrometer and the earth leads to a charge equalization 
on the capacitor plate and the effect is therefore not visible. The effect is not 
visible with a conventional multimeter. A plastic rod is used as the body, which 
was rubbed on a wool sweater so that it became charged. Then it is brought closer 
to the capacitor plate, the distance being varied several times. 

Fig. 20 below shows the time course of the voltage across the capacitor. The 
change in voltage with the distance between the rods can be clearly seen. The sign 
of the voltage also shows that the rod is positively charged. 

*Fig. 20*: **Influence** Time curve of the voltage on the capacitor with repeated
changes in the distance to the charged rod.  
                    ![Figure 20](images/elektrostatik_2.png)  

Now the demonstration of the electrical charge spoon follows. To do this, a metal ball is 
rubbed on a wool sweater and then the discharged capacitor plate is touched with it. The 
illustration shows the course of the voltage. The increase in the capacitor voltage  
upon contact with the sphere indicates the charge. With Q = C · U, a known 
capacitance of 1 nF and the measured voltage difference of −2.7 V, the transferred charge 
is determined to be −2.7 nC.

*Fig. 21*: **Electric Charge spoon** Time curve of the voltage on the capacitor when 
approaching and touching a charged ball. At approx. 66 s the capacitor is grounded 
so that the voltage is 0 V. When the charged sphere approaches, the amount of 
voltage on the capacitor increases due to influence. When the ball touches the 
capacitor plate (t ≈ 67.9 s), the voltage reaches a constant value.  
                    ![Figure 21](images/elektrostatik_3.png)  


&nbsp;<a name="kraftsensor"></a>
### 5.2 Force sensor

A force measurement is to be carried out using a load cell. It is checked whether the voltage 
applied to the load cell increases linearly with the attached mass, as one would expect.
The schematic layout of the experiment is shown in the Figure below.

*Fig. 22*: **force sensor** schematic structure  
                    ![Figure 22](images/kraft_aufbau.png)  

The load cell used can be rebuilt according to 
[these instructions](docs/Bauanleitung_Kraftsensor.pdf).  

First, the load cell is supplied with an operating voltage of U=5V and screwed 
to a device so that weights can be attached to it. The voltage difference between 
the two outputs of the load cell is a measure of the applied force. Since this 
difference is typically in the mV range, the voltage is amplified using the 
instrumentation amplifier. The output of the instrumentation amplifier is connected 
to input A0 of the ADC. Since the necessary gain factor is unknown, it is initially 
set small and then increased during the measurement until the signal is in a 
suitable value range. Since the polarity of the voltage is also unknown, a 
reference voltage is tapped and connected to the associated connection of the 
instrumentation amplifier. 

This shifts the output voltage by the value of the reference voltage so that 
negative voltages can be shifted to positive voltages. Approx. 2-3V can be used, 
whereby the exact value of the reference voltage is irrelevant, as this voltage is 
then subtracted again. To do this, the reference voltage is applied to input A1 of 
the ADC and A0 - A1 selected as the output.

Once the setup is complete, the measurement can be started and the amplification 
factor selected with different masses so that a voltage is visible. The gain factor 
here is A=18. While the measurement is in progress, pieces of weight up to 
500 g are hung on the load cell in 50 g increments. In addition, the voltage is 
taken up if no mass is attached.  
The measured values ​​are then exported and the stresses are assigned to the 
respective attached masses. By averaging the voltage values ​​over time during the 
time when the respective piece of mass was attached, a voltage value can be 
assigned to each mass. This results in ten voltage values ​​for the ten pieces of 
mass. It can be seen that the voltage is proportional to the attached 
mass. The voltage that is measured without an attached mass is subtracted from 
the other voltages as an offset voltage. After determining the compensation 
function, this load cell can be used as a scale for masses of up to 500 g.

*Fig. 23*: The voltage of the load cell increases with increasing force. The 
offset voltage that is applied without an attached mass is subtracted from the 
remaining voltage values. The measured values ​​are compatible with a straight line 
through the origin.  
                    ![Figure 23](images/kraft_ratio.png)  

The regression can either be carried out directly in *PhyPiDAQ* with the *ChanCalib*  
function, or the values are exported and then transferred to Excel, Python, etc. for
further processing. 

*Config file*:

*kraftsensor.daq:*
```yaml
DeviceFile: config/kraft_ADS1115Config.yaml   # 16 bit ADC, I2C bus
ChanLabels: ['Spannung']            # names for channels 
ChanUnits: ['V']         # units for channels 
ChanColors: [darkblue]      # channel colours in display

Interval: 0.05                 # logging interval         
NHistoryPoints: 20000          # number of points used in history buffer, time=NHistoryPoints*Interval = 2000*0.05 = 
100 seonds
DisplayModule: DataGraphs     # text, bar-graph, history and xy-view
Title: "Data from File"       # display title
DataFile:   null              #  null to disable 
CSVseparator: '   '            # field separator, set to ';' for German Excel   
```

*kraft_ADS1115Config.yaml:*
```yaml
DAQModule: ADS1115Config  
ADCChannels: [0]
DifModeChan: [true]
Gain: [1]
sampleRate: 860
```


&nbsp;<a name="photoeffekt"></a>
### 5.3 Photo effect

The photo effect is examined in more detail below. The resulting counter-voltage 
should be measured for six different wavelengths in the range from *λ = 360 nm* to 
λ=590 nm. Then the ratio *h/e*, where *h* is Planck's quantum and *e* is 
the elementary charge, should be determined. 

A mercury lamp is used as the light source because it also emits light in the UV 
range. The light beam is bundled with lenses and reduced to the respective 
wavelength with interference filters. When the photons hit the cathode, electrons 
are released and a positive excess charge is created on the initially neutrally 
charged plate. If electrons hit the opposite anode, it is negatively charged. The 
separation of charges between the anode and the cathode creates an increasing 
electric field, which slows down further electrons that fly from the cathode to 
the anode. In equilibrium, the breaking force is so great that even electrons 
no longer arrive at the anode with maximum kinetic energy. The voltage between the 
cathode and anode is then maximum. The maximum voltage then corresponds to the 
counter voltage.

The measuring method used here contains a capacitor connected in parallel to the 
photocell, which is charged by the photovoltage. The tension that arises 
corresponds to the counter-tension. This method has the advantage that a rather 
complex and laborious setting of the photocurrent can be dispensed with. As a 
result, this test can be carried out in a very short time and with high accuracy. 

On the hardware side, the voltage is measured with the electrometer, since a large 
internal resistance is required here in order not to falsify the measurement. A 
commercially available multimeter is therefore unsuitable. The circuit structure 
can be seen in the following figure:

*Fig. 24*: **Photoeffect** schematic structure  
                    ![Figure 24](images/photo_aufbau.png)  

The capacitor with *C=47µF* may have to be adjusted if the charging is too fast or too slow.


The following *config file* can be used in *PhyPiDAQ*. (The plots below were created by 
exporting the values from *PhyPiDAQ* as *.csv* and then reading them into a 
Python script. This can be done just as well e.g. , with an Excel table or something similar.)  

*photoeffekt.daq:*
```yaml
DeviceFile: config/photoeffekt_ADS1115Config.yaml   # 16 bit ADC, I2C bus
ChanLabels: ['Voltage']            # names for channels 
ChanUnits: ['V']         # units for channels 
ChanColors: [darkblue]      # channel colours in display

Interval: 0.05                 # logging interval         
NHistoryPoints: 20000          # number of points used in history buffer, time=NHistoryPoints*Interval = 2000*0.05 = 
100 seonds
DisplayModule: DataGraphs     # text, bar-graph, history and xy-view
Title: "Data from File"       # display title
DataFile:   null              #  null to disable 
CSVseparator: '   '            # field separator, set to ';' for German Excel   
```

*photoeffekt_ADS1115Config.yaml:*
```yaml
DAQModule: ADS1115Config  
ADCChannels: [0]
DifModeChan: [false]
Gain: [1]
sampleRate: 860
```
The measurement can now be started and the counter voltage is displayed, which 
results from the charging of the capacitor by the photo effect. The capacitor is 
connected to ground again for discharging.

The results obtained are summarized in the Figure below. 

*Fig. 25*: **Photo effect** Charging of a capacitor on a vacuum photocell for different wavelengths of the incident 
light  
                    ![Figure 25](images/photo_1.png)  

A number of interesting effects are worht mentioning:  
 
 - all voltages saturate at a fixed value depending on the color of the incident light
 - the rise time is different depending on the intensity of the light. 


To calculate the ratio *h/e*, the energy balance is first drawn up. The 
incident light with the wavelength *λ* has the frequency *ν=λc* and the 
energy *E<sub>light</sub>=hν*.  
After deducting the work function, the released electrons have the kinetic energy 
*E<sub>kin</sub>=E<sub>light</sub>-E_A*.  
For the energy of the electric field, *E<sub>field</sub>=U*e* applies, where *U* 
is the counter voltage and *e* is the elementary charge.  
In the stationary case, the energy of the electric field is the same as the kinetic 
energy, *E<sub>field</sub>=E<sub>kin</sub>*, so that when inserted, *U·e=h·ν−E_A* results.  
For the saturation voltage, *U = h/e · ν + e·A* applies.  

A graph showing the saturation voltage *U* as a function of the frequency *ν* 
of the incident light is shown in the Figure below. The slope of the indicated 
straight line, obtained via linear regression, corresponds to the ratio *h/e*.  
The y-axis intercept corresponds to the work function *E_A*, with a negative sign 
indicating that this physical work is needed to free an electron. 

*Fig. 26*: **Photoeffect** Saturation voltage versus frequency of light.  
                    ![Figure 26](images/photo_2.png)  

The deviation of *(h/e)<sub>measured</sub>* from the literature value of 
*h/e=4.14·10^(−15) Js/C* is only 3.5%, which indicates a very precise measurement 
at the percent-level precision. The work function for a potassium cathode is 
*E_A = 2.25 eV*. The y-intercept corresponds to *|e·U| = 1. 97eV*, 
which deviates from the best known value at the level of 10%.


