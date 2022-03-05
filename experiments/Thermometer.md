# Calibration of a non-linear temperature sensor

Temperature measurements are one of the most common tasks for digital recording. 
Very often, simple set-ups are used consisting of a temperature-dependent 
resistor connected in series to a reference resistor. Here, we use a so-called
NTC resistor made of semi-conducting material, which shows a falling electrical 
resistance when the temperature rises, hence the name: NTC = Negative Temperature
Coefficient. 

![](../Experimente/images/course/voltage_divider_NTC.PNG)

A very precise Analog-to-Digital Converter ("ADC") is used to read the 
temperature-dependent voltage at the middle connector of the voltage divider. 

The schematic layout of the experiment is shown here:

![](../Experimente/images/course/breadboard_ntc.PNG)

There still is one problem left: the voltage change does not depend linearly
on the Temperature change! This, however, is not a problem as we have a Raspberry 
Pi at hand. We first establish the relation between the ACD reading, the voltage 
and the temperature using a precise thermometer in a calibration experiment.
This results in a table that is used to calculate the temperature from the 
measured voltage. 

Her is the list of **Material**:

- 10 k&Omega; resistor 
- NTC-resitor (**N**egative **T**emperature **C**oefficient) *R<sub>25</sub>* = 10 k&Omega; 
- AD converter ADS1115
- Breadboard with power supply 
- Breadboard cables in different colors 
- Raspberry Pi 
- Ribbon cable 
- Electric kettle 
- Beakers 
- Thermometer 
- Glass rod for stirring 


**Procedure**:

Build the circuit on the breadboard. The table below shows how to connect the  
AD converter to the breadboard. 

| Connectors of AD-converter ADS1115 | Breadboard connectors / GPIO pin |
| ---------------------------------- | -------------------------------- |
| VDD                           | 5 V                                   |
| GND                           | 0 V                                   |
| SDL                           | GPIO-Pin SCL                          |
| SDA                           | GPIO-Pin SDA                          |
| A0                            | output of voltage divider             |

Next, we write a small *Python* program for data analysis, **thermometer.py**:

```python
import Adafruit_ADS1x15          # import library for AD-converter
import time                      # import "time".

adConverter = Adafruit_ADS1x15.ADS1115() # name for the AD converter object
  
while True: # loop
    adValue = adWandler.read_adc(0,2/3)      # read and store ADC value for channel A0 
    print("Voltage AD-Converter: ", adVAlue) # print it 
    time.sleep(1)                            # wait 1 s (Raspberry Pi "sleeps").
```

This program does the following:  
It queries the digitized signal value at connector A0 of the AD converter and outputs it. 
Then it waits a second and queries the next value, and so on.

- Note down the value displayed (approximately) at room temperature. 
  What happens when the NTC resistor is warmed up between your palms to hand temperature?
  Note down your observations.

- Now end the program by typing "Ctrl+c".


### Turning ADC output into voltage

The question now is: what do the observed values have to do with the measured voltage levels ?
To answer, we first need to know the resolution of our AD converter, i.e. "how high" a single 
step is. With each sample, the ADC assigns an integer number to the  analogue signal at the input. 
In order to determine the input voltage from the output value we just need to know what voltage  difference a stage corresponds to. 
The ADS1115 is capable of digitizing voltage values between 0 V - 6.114 V in 0 - 32767 steps.

- Calculate the voltage difference corresponding to one stage. This is the resolution, i.e. the
  smallest voltage change the ADC can detect. Note down this value !

- Complete the missing values in the table below.

     | stage |          | Voltage in V |
     | ----- | :------: | ------------ |
     | 0     | &#x27F9; | 0.           |
     | 32767 | &#x27F9; | 6.114        |
     | 1     | &#x27F9; |              |
     | 518   | &#x27F9; |              |
     | 16383 | &#x27F9; |              |

It is easy to build this information into the *Pyhton* code in order to
directly display the voltage. 

- complete *thermometer.py* to display the measured voltage.


### From Voltage to temperature

We have not reached our goal yet; the missing step is to relate the voltages
to temperatures. This step is called "calibration". 

So, let us perform such a calibration. We start with hot water of a temperature of
approx. 50 °C, insert a thermometer and the NTC resistor. By adding cold water and
carefully stirring with a glass rod temperatures down to 20 °C can be obtained. 

- note down the water temperatures and the voltages in the table below:

  |                       |  1.    |   2.   |   3.   |   4.   |
  | --------------------- | ------ | ------ | ------ | ------ |
  | Temperature *T* in °C |        |        |        |        |
  | Voltage *U* in V      |        |        |        |        |


- Draw the pairs of values in a diagram and connect the measured points 
  to form a smooth curve. 

- Read from the diagram the approximate expected digitized voltage value for 
  a temperature of 35 °C and note it down.

We are now very close to our goal, namely building a digital thermometer. What we 
have so far is working, but not very convenient. Some software support helps here.

So, let the Raspberry Pi calculate a function connecting our calibration points 
with a smooth curve. Fortunately, there exists a library for this job, which we
will import on our program. Using this function we can calculate the corresponding 
temperature for each measured digital voltage value. The more pairs of values we 
have for the calibration and the more precisely they were determined, the more 
precise are the temperature values determined this way.

Let us complete the code in **thermometer.py**:

```python
import Adafruit_ADS1x15                        # import library for AD-converter
import time                                    # import "time"
from scipy.interpolate import UnivariateSpline # library for interpolation curve

adConverter = Adafruit_ADS1x15.ADS1115() # name for the AD converter object
resolution = 6.114/32767 # resolution of AD converter  

U = [U1, U2, U3 , U4]             # voltages in ascending order and ...
T = [T1, T2, T3 , T4]             # ... corresponding temperatures from calibration 
calibFunc = UnivariateSpline(U,T) # calculate calibration function

while True: # loop
    adVoltage = adConverter.read_adc(0,2/3) * resolution  # read and store voltage A0 
    temperature = calibFunc(adVoltage)                    # calculate temperature from voltage
    temperature = round(float(temperatur),1)              # round to one digit
    print("Temperature: ", temperature, " °C")            # print result
    time.sleep(1)                                         # wait 1 s (Raspberry Pi "sleeps").
```

- Enter the values U1 - U4 and T1 -T4 from your calibration data;
- Test the digital thermometer by running the program.

If you are done, end the program by typing "ctrl + c".
