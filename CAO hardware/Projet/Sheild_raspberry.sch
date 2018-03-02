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
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L RFM95 LoRa?
U 1 1 5A952813
P 6500 2850
F 0 "LoRa?" H 6500 3100 60  0001 C TNN
F 1 "RFM95" H 6500 3250 60  0000 C CNN
F 2 "" H 6500 3250 60  0001 C CNN
F 3 "" H 6500 3250 60  0001 C CNN
	1    6500 2850
	1    0    0    -1  
$EndComp
$Comp
L Raspberry_Pi_2_3 J?
U 1 1 5A952827
P 4200 2850
F 0 "J?" H 4900 1600 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 3800 3750 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x20" H 5200 4100 50  0001 C CNN
F 3 "" H 4250 2700 50  0001 C CNN
	1    4200 2850
	1    0    0    -1  
$EndComp
$Comp
L Conn_Coaxial J?
U 1 1 5A952AD2
P 6450 3850
F 0 "J?" H 6460 3970 50  0000 C CNN
F 1 "Conn_Coaxial" V 6565 3850 50  0000 C CNN
F 2 "" H 6450 3850 50  0001 C CNN
F 3 "" H 6450 3850 50  0001 C CNN
	1    6450 3850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7000 3050 7150 3050
Wire Wire Line
	7150 3050 7150 4200
Wire Wire Line
	7150 4200 6450 4200
Wire Wire Line
	6450 4200 6450 4000
Wire Wire Line
	5450 2850 5100 2850
Wire Wire Line
	5450 2850 5450 2450
Wire Wire Line
	5450 2450 6000 2450
Wire Wire Line
	5100 2950 5550 2950
Wire Wire Line
	5550 2950 5550 2550
Wire Wire Line
	5550 2550 6000 2550
Wire Wire Line
	6000 2650 5650 2650
Wire Wire Line
	5650 2650 5650 3050
Wire Wire Line
	5650 3050 5100 3050
Wire Wire Line
	7000 2650 7150 2650
Wire Wire Line
	7150 2650 7150 1400
Wire Wire Line
	7150 1400 4400 1400
Wire Wire Line
	4400 1400 4400 1550
Wire Wire Line
	6650 3850 6850 3850
Wire Wire Line
	6850 3850 6850 3200
Wire Wire Line
	6850 3200 6000 3200
Wire Wire Line
	6000 3200 6000 3050
Wire Wire Line
	3800 4150 4500 4150
Wire Wire Line
	4450 4150 4450 4350
Wire Wire Line
	4450 4350 3100 4350
Wire Wire Line
	3100 4350 3100 1300
Wire Wire Line
	3100 1300 6000 1300
Wire Wire Line
	6000 1300 6000 2350
Connection ~ 4450 4150
Wire Wire Line
	5100 2750 6000 2750
Wire Wire Line
	6000 2850 5800 2850
Wire Wire Line
	5800 2850 5800 3250
Wire Wire Line
	5800 3250 5100 3250
$EndSCHEMATC
