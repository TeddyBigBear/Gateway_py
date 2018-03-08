EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:switches
LIBS:relays
LIBS:motors
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
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:rfm95
LIBS:Sheild_raspberry-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Sheild Gateway"
Date ""
Rev "1.0"
Comp "Polytech'"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Raspberry_Pi_2_3 J1
U 1 1 5A9C305C
P 3150 3450
F 0 "J1" H 3850 2200 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 2750 4350 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Angled_2x20_Pitch2.54mm" H 4150 4700 50  0001 C CNN
F 3 "" H 3200 3300 50  0001 C CNN
	1    3150 3450
	1    0    0    -1  
$EndComp
$Comp
L RFM95 LoRa1
U 1 1 5A9C30A1
P 7400 2750
F 0 "LoRa1" H 7400 3000 60  0001 C TNN
F 1 "RFM95" H 7400 3150 60  0000 C CNN
F 2 "RF_Modules:Hopref_RFM9XW_SMD" H 7400 3150 60  0001 C CNN
F 3 "" H 7400 3150 60  0001 C CNN
	1    7400 2750
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR01
U 1 1 5A9C3168
P 8150 2500
F 0 "#PWR01" H 8150 2350 50  0001 C CNN
F 1 "+3.3V" H 8150 2640 50  0000 C CNN
F 2 "" H 8150 2500 50  0001 C CNN
F 3 "" H 8150 2500 50  0001 C CNN
	1    8150 2500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 5A9C3185
P 8400 3000
F 0 "#PWR02" H 8400 2750 50  0001 C CNN
F 1 "GND" H 8400 2850 50  0000 C CNN
F 2 "" H 8400 3000 50  0001 C CNN
F 3 "" H 8400 3000 50  0001 C CNN
	1    8400 3000
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR03
U 1 1 5A9C31A1
P 6800 3050
F 0 "#PWR03" H 6800 2800 50  0001 C CNN
F 1 "GND" H 6800 2900 50  0000 C CNN
F 2 "" H 6800 3050 50  0001 C CNN
F 3 "" H 6800 3050 50  0001 C CNN
	1    6800 3050
	1    0    0    -1  
$EndComp
Text Label 6650 2350 0    60   ~ 0
MISO
Text Label 6650 2450 0    60   ~ 0
MOSI
Text Label 6650 2550 0    60   ~ 0
CLK
Text Label 6650 2650 0    60   ~ 0
CS
Text Label 6650 2750 0    60   ~ 0
RESET
Text Label 8000 2950 0    60   ~ 0
ANT
$Comp
L GND #PWR04
U 1 1 5A9C321A
P 2750 4950
F 0 "#PWR04" H 2750 4700 50  0001 C CNN
F 1 "GND" H 2750 4800 50  0000 C CNN
F 2 "" H 2750 4950 50  0001 C CNN
F 3 "" H 2750 4950 50  0001 C CNN
	1    2750 4950
	1    0    0    -1  
$EndComp
Text Label 4350 3350 0    60   ~ 0
CS
Text Label 4250 3450 0    60   ~ 0
MISO
Text Label 4250 3550 0    60   ~ 0
MOSI
Text Label 4300 3650 0    60   ~ 0
CLK
$Comp
L +3.3V #PWR05
U 1 1 5A9C33FB
P 3250 1950
F 0 "#PWR05" H 3250 1800 50  0001 C CNN
F 1 "+3.3V" H 3250 2090 50  0000 C CNN
F 2 "" H 3250 1950 50  0001 C CNN
F 3 "" H 3250 1950 50  0001 C CNN
	1    3250 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6900 2350 6650 2350
Wire Wire Line
	6900 2450 6650 2450
Wire Wire Line
	6900 2550 6650 2550
Wire Wire Line
	6900 2650 6650 2650
Wire Wire Line
	6900 2750 6650 2750
Wire Wire Line
	6900 2950 6800 2950
Wire Wire Line
	6800 2950 6800 3050
Wire Wire Line
	7900 2950 8150 2950
Wire Wire Line
	7900 2550 8150 2550
Wire Wire Line
	8150 2550 8150 2500
Wire Wire Line
	7900 2850 8400 2850
Wire Wire Line
	8400 2850 8400 3000
Wire Wire Line
	2750 4750 2750 4950
Wire Wire Line
	2750 4750 3050 4750
Connection ~ 2850 4750
Connection ~ 2950 4750
Wire Wire Line
	4050 3350 4450 3350
Wire Wire Line
	4050 3450 4450 3450
Wire Wire Line
	4050 3550 4450 3550
Wire Wire Line
	4050 3650 4450 3650
Wire Wire Line
	3250 2150 3250 1950
Wire Wire Line
	2250 3850 1850 3850
Text Label 2100 3850 2    60   ~ 0
RESET
$Comp
L Conn_Coaxial J2
U 1 1 5A9C3498
P 7250 4000
F 0 "J2" H 7260 4120 50  0000 C CNN
F 1 "Conn_Coaxial" V 7365 4000 50  0000 C CNN
F 2 "Connectors_Molex:Molex_SMA_Jack_Edge_Mount" H 7250 4000 50  0001 C CNN
F 3 "" H 7250 4000 50  0001 C CNN
	1    7250 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	7100 4000 6800 4000
Wire Wire Line
	7250 4200 7250 4300
$Comp
L GND #PWR06
U 1 1 5A9C36A6
P 7250 4300
F 0 "#PWR06" H 7250 4050 50  0001 C CNN
F 1 "GND" H 7250 4150 50  0000 C CNN
F 2 "" H 7250 4300 50  0001 C CNN
F 3 "" H 7250 4300 50  0001 C CNN
	1    7250 4300
	1    0    0    -1  
$EndComp
Text Label 6800 4000 0    60   ~ 0
ANT
$EndSCHEMATC
