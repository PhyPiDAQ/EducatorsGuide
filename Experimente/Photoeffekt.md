# *PhyPiDAQ*: Experimente zum Photoeffekt

Eine im Vergleich zur klassischen Gegenspannungsmethode einfache Variante zur  quantitativen Behandlung des Photoeffekts ist mit Hilfe eines Elektrometerverstärkers 
möglich. Schaltet man einen Kondensator parallel zu einer mit Licht einer bekannten 
festen Wellenlänge beleuchteten Vakuumphotozelle, so lädt sich der Kondensator so lange 
auf, bis auch die schnellsten der ausgelösten Elektronen nicht mehr gegen die
Kondensatorspannung anlaufen können. Mit einem modernen Operationsverstärker 
mit sehr hohem Innenwiderstand kann diese Spannung problemlos gemessen werden, ohne
den Kondensator zu entladen. Ein Schema dieser einfachen Messung ist hier gezeigt: 

*Abb. 1*:  **Photoeffekt**: Prinzip zur Messung der Gegenspannung mit einem Kondensator    
                    ![Abb. 1](images/Photoeffekt_prinzip.png)  


Im Folgenden wird der Photoeffekt quantitativ untersucht. Für sechs verschiedene 
Wellenlängen im Bereich von λ = 360 nm bis λ = 590 nm soll die sich jeweils ergebende 
Gegenspannung gemessen werden. Anschließend soll aus der Messreihe das Verhältnis 
*h/e* bestimmt werden, wobei *h* das Plancksche Wirkungsquantum und *e* die Elementarladung ist. 

Als Lichtquelle wird eine Quecksilber-Lampe verwendet, da diese auch im UV-Bereich Licht emittiert. Mit Linsen wird der 
Lichtstrahl gebündelt und mit Interferenzfiltern die jeweilige Wellenlänge ausgewählt. Durch das Auftreffen der 
Photonen auf der Kathode werden Elektronen herausgelöst und auf der zunächst neutral geladenen Platte stellt sich ein 
positiver Ladungsüberschuss ein. Treffen Elektronen auf die gegenüberliegende Anode, so wird diese negativ geladen. 
Durch die Ladungstrennung zwischen Anode und Kathode entsteht ein ansteigendes elektrisches Feld, welches weitere 
Elektronen, die von der Kathode zur Anode fliegen, abbremst. Im Gleichgewicht ist die Bremskraft so groß, dass selbst 
Elektronen mit maximaler kinetischer Energie nicht mehr bei der Anode ankommen. Die Spannung zwischen Kathode und Anode 
ist dann maximal. Die maximale Spannung entspricht dann der Gegenspannung.  

Die Messmethode, die hier verwendet wird, enthält einen parallel zur Photozelle geschalteten Kondensator, der sich 
durch die Photospannung auflädt. Die Spannung, die sich einstellt, entspricht der Gegenspannung. Diese Methode hat den 
Vorteil,  dass auf eine eher aufwendige und mühselige Einstellung des Photostroms verzichtet werden kann. Dadurch kann 
dieser Versuch in sehr kurzer Zeit und mit hoher Genauigkeit bewerkstelligt werden.   

Hardwareseitig wird die Spannung mit dem Elektrometer gemessen, da hier ein  großer Innenwiderstand benötigt wird, um 
die Messung nicht zu verfälschen.  Ein handelsübliches Multimeter ist daher ungeeignet. Der Schaltaufbau ist in der 
nachfolgenden Abbildung zu sehen:

*Abb. 2*:  **Photoeffekt**: schematischer Aufbau  
                    ![Abb. 2](images/photo_aufbau.png)  

Der Kondensator mit *C=47µF* muss ggf. angepasst werden, falls die Aufladung zu schnell oder zu langsam erfolgt.

In *PhyPiDAQ* kann folgende Config verwendet werden. (Die Plots weiter unten wurden erstellt, indem die Werte von 
*PhyPiDAQ* als *.csv* exportiert und anschließend in einem Python Script eingelesen wurden. Dies kann für die 
Mittelstufe beispielsweise genauso gut mit einer Exceltabelle oder ähnlichem erstellt werden.)

***photoeffekt.daq:**

```yaml
DeviceFile: config/photoeffekt_ADS1115Config.yaml   # 16 bit ADC, I2C bus
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

*photoeffekt_ADS1115Config.yaml:*
```yaml
DAQModule: ADS1115Config  
ADCChannels: [0]
DifModeChan: [false]
Gain: [1]
sampleRate: 860
```
Die Messung kann nun gestartet werden und die Gegenspannung wird dargestellt, welche sich  aus der Aufladung des 
Kondensators durch den Photoeffekt ergibt. Zum Entladen wird der Kondensator wieder mit Masse verbunden.  

Die Grafik unten zeigt den jeweiligen Spannungsverlauf für verschiedene Farben des einfallenden Lichts. Wichtige 
Beobachtungen sind: 
  - die Spannungen über dem Kondensator saturieren abhängig von der Farbe
  - der Spannungsanstieg ist jeweils unterschiedlich und hängt von der Lichtintensität ab.

*Abb. 3*:  **Photoeffekt**: Aufladung eines Kondensators an einer Vakuum-Photozelle für verschiedene Wellenlängen des 
einfallenden Lichts  
                    ![Abb. 3](images/photo_1.png)  


Um das Verhältnis *h/e* zu berechnen, wird zunächst die Energiebilanz aufgestellt.  
Das einfallende Licht mit der Wellenlänge *λ* hat die Frequenz *f = λc* und die Energie
 *E<sub>Licht</sub> = hf*.  
Die herausgelösten Elektronen haben nach Abzug der Austrittsarbeit die kinetische Energie
 *E<sub>kin</sub> = E<sub>Licht</sub> − E<sub>A</sub>*.  
Für die von den Elektronen im elektrischen Feld aufgenommene Energei gilt:  
*E<sub>Feld</sub> = U · e*,
wobei *U* die Gegenspannung und *e* die Elementarladung ist.  
Im  stationären Fall ist die Energie des elektrischen Feldes gleich groß wie die kinetische Energie *E<sub>Feld</sub> = 
E<sub>kin</sub>*, sodass sich eingesetzt 
*U·e=hν−E<sub>A</sub>* 
ergibt.  
Für die Spannung *U* gilt schließlich: *U = h/e · f + e·A*.

Das Verhältnis *h/e* entspricht  der Steigung im *U*−*f*-Diagramm in der Abbildung unten. 
Der y-Achsenabschnitt entspricht  der Austrittsarbeit *E<sub>A</sub>*, wobei ein negatives Vorzeichen dafür steht, dass 
diese  Arbeit aufgebracht werden muss. 
Die Abweichung von *(h/e)<sub>gemessen</sub>* zum Literaturwert von *h/e = 4,14 ·10−15 Js/C* beträgt 3,5%, für den 
betriebenen Aufwand also eine beachtliche Genauigkeit.  
Die Austrittsarbeit für eine Kalium-Kathode beträgt *E<sub>A</sub> = 2,25 eV*. 
Der y-Achsenabschnitt  entspricht *|eU| = 1,97eV*. Da hier keine weiteren Effekte wie zum Beispiel  Kontaktspannungen 
berücksichtigt werden, ist die Bestimmung der Austrittsarbeit mit diesem Verfahren grundsätzlich nur mit größeren 
Unsicherheiten möglich.  
Weiter lässt sich aus der Kondensatoraufladung  in der Abbildung unten der Photostrom berechnen. Es ist zu sehen, dass 
dieser im  pA-Bereich liegt. Bei 590 nm Wellenlänge war der Strom am kleinsten, was sich an der verhältnismäßig 
langsamen Aufladung zeigt.

*Abb. 4*:  **Photoeffekt**:  Gegenspannung gegen Frequenz des Lichts, aufgetragen mit linearer Regression. Die 
Geradensteigung entspricht dem Verhältnis *h/e*.  
                    ![Abb. 4](images/photo_2.png)  

