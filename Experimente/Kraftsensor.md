# *PhyPiDAQ*: Experimente mit einer Wägezelle als Kraftsensor

Mithilfe einer Wägezelle wird eine Kraftmessung durchgeführt. Dabei  wird zunächst überprüft, ob die 
an der Wägezelle anliegende Spannung linear mit der angehängten Masse ansteigt. Diese Messung dient
zur Kalibration der Kraftmessung.  

Da die relative Änderung des Widerstands von Dehnmessstreifen nur klein ist, wird zu Messung eine
Wheatsone-Brücke aus vier Dehnmessstreifen verwendet. Weil das Signal auch dann noch klein ist,
empfiehlt es sich, einen Instrumentenverstärker zu verwenden, wie er in Abb. 1 gezeigt. ist.

*Abb. 1*:  **Instrumentenverstärker** zur Messung kleiner Spannungen.  
                    ![Abb. 1](../Schematics/Instrumentenverstaerker_schematic.png)  

Wenn das Signal mit einem an den Raspberry Pi angeschlossenen Analog-Digital-Wandler aufgezeichnet
werden soll, kann man den Referenz-Eingang der Instrumentenverstärkers mit einer Spannung belegen,
die die Null-Lage festlegt und so die Ausgangsspannung in den Bereich von 0-5V anhebt. 

## Kalibration eines Dehnmessstreifen-Kraftmessers

Der schematische Aufbau unter Verwendung der im Messkoffer vorhandenen Messplatine ist 
nachfolgend dargestellt:

*Abb. 2*:  **Kraftsensor** schematischer Aufbau  
                    ![Abb. 2](images/kraft_aufbau.png)  

Die verwendete Wägezelle kann nach [dieser Anleitung](docs/Bauanleitung_Kraftsensor.pdf) nachgebaut werden. 

Zunächst wird die Wägezelle mit einer Betriebsspannung von *U=5V* versorgt und an eine Vorrichtung geschraubt, sodass 
Massestücke daran angehängt werden können. Die Spannungsdifferenz der beiden Ausgänge der Wägezelle ist ein Maß für die 
anliegende Kraft. Da dieser Unterschied typischerweise im *mV*-Bereich liegt, wird eine Verstärkung der Spannung mit 
dem Instrumentenverstärker vorgenommen. Der Ausgang des Instrumentenverstärkers wird mit dem Eingang A0 des ADC 
verbunden. Da der notwendige Verstärkungsfaktor unbekannt ist, wird dieser zunächst  klein eingestellt und während der 
Messung anschließend erhöht, bis sich das Signal in einem geeigneten Wertebereich befindet. Da die Polarität der 
Spannung ebenfalls unbekannt ist, wird eine Referenzspannung abgegriffen und mit dem dazugehörigen Anschluss des 
Instrumentenverstärkers verbunden. 
Diese verschiebt die Ausgangsspannung um den Wert der Referenzspannung, sodass negative Spannungen zu positiven 
Spannungen verschoben werden können. Es können ca. 2-3V verwendet werden, wobei der genaue Wert der Referenzspannung  
unerheblich ist, da diese Spannung anschließend wieder abgezogen wird. Dazu wird die Referenzspannung an den Eingang A1 
des ADC angelegt und A0 - A1 als Ausgabe gewählt.  

Ist der Aufbau abgeschlossen, so kann die Messung gestartet und mit verschiedenen Massen der Verstärkungsfaktor so 
gewählt werden, dass eine Spannung sichtbar ist. Der Verstärkungsfaktor beträgt hier *A = 18*. Bei laufender Messung 
werden nacheinander Massestücke bis 500 g in 50 g Schritten an die Wägezelle gehängt.  
Des Weiteren wird die Spannung aufgenommen, wenn kein Massestück angehängt ist.  Anschließend werden die Messwerte 
exportiert und die Spannungen den jeweiligen angehängten Massen zugeordnet. Durch zeitliches Mitteln der Spannungswerte 
während der Zeit, als das jeweilige Massestück angehängt war, kann jeder Masse ein Spannungswert zugeordnet werden. Es 
ergeben sich somit zehn Spannungswerte zu den  zehn Massestücken. Es ist zu erkennen, dass die Spannung proportional  
zur angehängten Masse ist. Die Spannung, welche gemessen wird, ohne dass ein Massestück angehängt ist, wird als 
Offset-Spannung von den anderen Spannungen abgezogen. Nach Bestimmung der Ausgleichsfunktion kann diese Wägezelle somit 
als Waage für Massen bis 500 g eingesetzt werden.  

*Abb. 3*:  Die Spannung an der Wägezelle steigt mit zunehmender Kraft an.  
Die Offset-Spannung, welche ohne ein angehängtes Massestück anliegt, wird von den 
restlichen Spannungswerten abgezogen. 
Die gemessenen Werte sind mit einer Ursprungsgeraden kompatibel.  
                    ![Abb. 3](images/kraft_ratio.png)  
 
Die Interpolation der Messpwerte kann entweder direkt in *PhyPiDAQ* mit der Funktion *ChanCalib* 
vorgenommen werden, oder die Werte werden exportiert und anschließend in Excel,  Python, ect. 
weiter verarbeitet.  

Konfigurtionsdatei **kraftsensor.daq:**

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

**kraft_ADS1115Config.yaml:**

```yaml
DAQModule: ADS1115Config  
ADCChannels: [0]
DifModeChan: [true]
Gain: [1]
sampleRate: 860
```
