EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:opto
LIBS:rfm95
LIBS:raspberrypi-gpio-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "15 nov 2012"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CONN_13X2 P1
U 1 1 50A55ABA
P 4800 3150
F 0 "P1" H 4800 3850 60  0000 C CNN
F 1 "CONN_13X2" V 4800 3150 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x13" H 4800 2450 30  0000 C CNN
F 3 "" H 4800 3150 60  0001 C CNN
	1    4800 3150
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR01
U 1 1 50A55B18
P 4300 2400
F 0 "#PWR01" H 4300 2250 50  0001 C CNN
F 1 "+3.3V" H 4300 2540 50  0000 C CNN
F 2 "" H 4300 2400 50  0000 C CNN
F 3 "" H 4300 2400 50  0000 C CNN
	1    4300 2400
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR02
U 1 1 50A55B2E
P 5300 2400
F 0 "#PWR02" H 5300 2250 50  0001 C CNN
F 1 "+5V" H 5300 2540 50  0000 C CNN
F 2 "" H 5300 2400 50  0000 C CNN
F 3 "" H 5300 2400 50  0000 C CNN
	1    5300 2400
	1    0    0    -1  
$EndComp
NoConn ~ 5200 2650
Text Label 3650 2650 0    60   ~ 0
GPIO0(SDA)
Text Label 3650 2750 0    60   ~ 0
GPIO1(SCL)
Text Label 3650 2850 0    60   ~ 0
GPIO4
NoConn ~ 4400 2950
Text Label 3650 3050 0    60   ~ 0
GPIO17
Text Label 3650 3150 0    60   ~ 0
GPIO21
Text Label 3650 3250 0    60   ~ 0
GPIO22
NoConn ~ 4400 3350
Text Label 3650 3450 0    60   ~ 0
GPIO10(MOSI)
Text Label 3650 3550 0    60   ~ 0
GPIO9(MISO)
Text Label 3650 3650 0    60   ~ 0
GPIO11(SCLK)
NoConn ~ 4400 3750
$Comp
L GND #PWR03
U 1 1 50A55C3F
P 5300 3850
F 0 "#PWR03" H 5300 3600 50  0001 C CNN
F 1 "GND" H 5300 3700 50  0000 C CNN
F 2 "" H 5300 3850 50  0000 C CNN
F 3 "" H 5300 3850 50  0000 C CNN
	1    5300 3850
	1    0    0    -1  
$EndComp
Text Label 5900 2850 2    60   ~ 0
TXD
Text Label 5900 2950 2    60   ~ 0
RXD
Text Label 5900 3050 2    60   ~ 0
GPIO18
NoConn ~ 5200 3150
Text Label 5900 3250 2    60   ~ 0
GPIO23
Text Label 5900 3350 2    60   ~ 0
GPIO24
NoConn ~ 5200 3450
Text Label 5900 3550 2    60   ~ 0
GPIO25
Text Label 5900 3650 2    60   ~ 0
GPIO8(CE0)
Text Label 5900 3750 2    60   ~ 0
GPIO7(CE1)
$Comp
L RFM95 LoRa1
U 1 1 5A99D138
P 4950 5500
F 0 "LoRa1" H 4950 5750 60  0001 C TNN
F 1 "RFM95" H 4950 5900 60  0000 C CNN
F 2 "" H 4950 5900 60  0001 C CNN
F 3 "" H 4950 5900 60  0001 C CNN
	1    4950 5500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 5A99D295
P 5800 5700
F 0 "#PWR04" H 5800 5450 50  0001 C CNN
F 1 "GND" H 5800 5550 50  0000 C CNN
F 2 "" H 5800 5700 50  0000 C CNN
F 3 "" H 5800 5700 50  0000 C CNN
	1    5800 5700
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR05
U 1 1 5A99D2D9
P 5800 5100
F 0 "#PWR05" H 5800 4950 50  0001 C CNN
F 1 "+3.3V" H 5800 5240 50  0000 C CNN
F 2 "" H 5800 5100 50  0000 C CNN
F 3 "" H 5800 5100 50  0000 C CNN
	1    5800 5100
	1    0    0    -1  
$EndComp
$Comp
L LED D1
U 1 1 5A99D338
P 3200 2550
F 0 "D1" H 3200 2650 50  0000 C CNN
F 1 "LED" H 3200 2450 50  0000 C CNN
F 2 "LEDs:LED-L1T2_LUMILEDS" H 3200 2550 50  0001 C CNN
F 3 "" H 3200 2550 50  0001 C CNN
	1    3200 2550
	0    -1   -1   0   
$EndComp
$Comp
L +5V #PWR06
U 1 1 5A99D3D2
P 3200 1700
F 0 "#PWR06" H 3200 1550 50  0001 C CNN
F 1 "+5V" H 3200 1840 50  0000 C CNN
F 2 "" H 3200 1700 50  0000 C CNN
F 3 "" H 3200 1700 50  0000 C CNN
	1    3200 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 2400 4300 2550
Wire Wire Line
	4300 2550 4400 2550
Wire Wire Line
	5300 2400 5300 2550
Wire Wire Line
	5300 2550 5200 2550
Wire Wire Line
	4400 2750 3650 2750
Wire Wire Line
	3200 2850 4400 2850
Wire Wire Line
	4400 3050 3650 3050
Wire Wire Line
	4400 3150 3650 3150
Wire Wire Line
	3000 3250 4400 3250
Wire Wire Line
	3100 3450 4400 3450
Wire Wire Line
	3200 3550 4400 3550
Wire Wire Line
	3300 3650 4400 3650
Wire Wire Line
	5300 3850 5300 2750
Wire Wire Line
	5300 2750 5200 2750
Wire Wire Line
	5200 2850 5900 2850
Wire Wire Line
	5200 2950 5900 2950
Wire Wire Line
	5200 3050 5900 3050
Wire Wire Line
	5200 3250 5900 3250
Wire Wire Line
	5200 3350 5900 3350
Wire Wire Line
	5200 3550 5900 3550
Wire Wire Line
	5200 3650 6100 3650
Wire Wire Line
	5200 3750 5900 3750
Wire Wire Line
	3100 3450 3100 5200
Wire Wire Line
	3100 5200 4450 5200
Wire Wire Line
	4450 5100 3200 5100
Wire Wire Line
	3200 5100 3200 3550
Wire Wire Line
	3300 5300 4450 5300
Wire Wire Line
	3300 5300 3300 3650
Wire Wire Line
	4450 5400 4200 5400
Wire Wire Line
	4200 5400 4200 4150
Wire Wire Line
	4200 4150 6100 4150
Wire Wire Line
	6100 4150 6100 3650
Wire Wire Line
	5450 5600 5800 5600
Wire Wire Line
	5800 5600 5800 5700
Wire Wire Line
	5800 5100 5800 5300
Wire Wire Line
	5800 5300 5450 5300
Wire Wire Line
	4450 5500 3000 5500
Wire Wire Line
	3000 5500 3000 3250
Wire Wire Line
	3200 1700 3200 1950
Wire Wire Line
	3500 2650 4400 2650
Wire Wire Line
	3200 2700 3200 2850
$Comp
L R R1
U 1 1 5A99D879
P 3200 2100
F 0 "R1" V 3280 2100 50  0000 C CNN
F 1 "R" V 3200 2100 50  0000 C CNN
F 2 "Resistors_SMD:R_0201" V 3130 2100 50  0001 C CNN
F 3 "" H 3200 2100 50  0001 C CNN
	1    3200 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3200 2250 3200 2400
$EndSCHEMATC
