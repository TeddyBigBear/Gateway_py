#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Auteur : SJ
Date : janvier 18
Fonction : lecture d'une trame et récupération des données
"""

import os
import time
import datetime
from operator import truediv
from GestionFichier import *
from GestionAck import *

#constantes
path="trameExemple.txt"
pathLog="log.txt"
DataEmpty=""
pathSiteWeb="http://vps503149.ovh.net/~ruche/"
requetePHP=""

#fonctions
def ConversionDirectionVent(directionVentBrute):
	switcher = {
		0: 0,
        1: 22.5,
        2: 45,
        3: 67.5,
        4: 90,
        5: 112.5,
        6: 135,
        7: 157.5,
        8: 180,
        9: 202.5,
        10: 225,
        11: 247.5,
        12: 270,
        13: 292.5,
        14: 315,
        15: 337.5,
	}
	return switcher.get(directionVentBrute, "Nombre invalide")


#ATTENTION : la taille des données pour chaque paramètre est codé en dur !!! 
def Decoupage_Trame_Station(ligne):
	offsetPression = 800
	offsetSolaire = 120000
	impulsionPluviometrie = 0.2794
	donneesTrame=[]
 	
	donneesTrame.append("type=M")

	for i in range(16,len(ligne)):

		if (ligne[i] == "U"):
			#2 chiffres, valeurs : 0x00 à 0x96 (décimal: 0,0 à 15,0)
			tensionBatterie = ligne[i+1:i+3]
			tensionBatterieDec = int(tensionBatterie, 16)
			#pour nombre à virgule
			tensionBatterieDec = truediv(tensionBatterieDec,10)
			donneesTrame.append("vbat="+str(tensionBatterieDec))

		if (ligne[i] == "S"):
			#2 chiffres, valeurs : 0x00 à 0x64 (décimal: 0 à 100%)
			solaire = ligne[i+1:i+3]
			solaireDec = int(solaire, 16) #conversion hexa en decimal
			solaireDec = solaireDec + offsetSolaire
			donneesTrame.append("sol="+str(solaireDec))

		if (ligne[i] == "T"):
			#3 chiffres, valeurs : 
			#nombre positif : 0x000 à 0x320 (décimal: 0,0 à 80,0°)
			#nombre négatif : 0xFFF à 0xE6F (décimal: -1,0 à -40,0°)
			temperature = ligne[i+1:i+4]
			temperatureDec = int(temperature, 16)
			print 'temp decimal : ' + str(temperatureDec)
			#gestion nombre négatif :
			if(3695<=temperatureDec<=4095):
				temperatureDec=temperatureDec-4096;
			temperatureDec = truediv(temperatureDec,10)
			print 'temp division par 10 : ' + str(temperatureDec)
			donneesTrame.append("temp_capteur="+str(temperatureDec))

		if (ligne[i] == "H"):
			#2 chiffres, valeurs : 0x00 à 0x64 (décimal: 0 à 100%)
			hygrometrie = ligne[i+1:i+3]
			hygrometrieDec = int(hygrometrie, 16)
			donneesTrame.append("hygro_capteur="+str(hygrometrieDec))

		if (ligne[i] == "L"):
			#2 chiffres, valeurs : 0x00 à 0xFF (décimal: 0 à 255)
			pluviometrie = ligne[i+1:i+3]
			pluviometrieDec = int(pluviometrie, 16)
			pluviometrieDec = pluviometrieDec*impulsionPluviometrie
			donneesTrame.append("pluvio="+str(pluviometrieDec))

		if (ligne[i] == "R"):
			#2 chiffres, valeurs : 0x00 à 0xFF (décimal: 0 à 255)
			rafaleVent = ligne[i+1:i+3]
			rafaleVentDec = int(rafaleVent, 16)
			donneesTrame.append("vent="+str(rafaleVentDec))

		if (ligne[i] == "V"):
			#2 chiffres, valeurs : 0x00 à 0xFF (décimal: 0 à 255)
			anemometre = ligne[i+1:i+3]
			anemometreDec = int(anemometre, 16)
			donneesTrame.append("vent_vit_max="+str(anemometreDec))

		if (ligne[i] == "P"):
			#3 chiffres, valeurs : 0x320 à 0x41F (décimal: 800 à 1050)
			pression = ligne[i+1:i+4]
			pressionDec = int(pression, 16)
			pressionDec = pressionDec + offsetPression
			donneesTrame.append("pres="+str(pressionDec))

		if (ligne[i] == "X"):
			#1 chiffre, valeurs : 0x0 à 0xF (décimal: 0 à 15)
			directionVent = ligne[i+1:i+2]
			directionVentDec = int(directionVent, 16)
			directionVentDec = ConversionDirectionVent(directionVentDec)
			#print directionVentDec
			donneesTrame.append("dirv="+str(directionVentDec))

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame

def Decoupage_Trame_RucherInterne(ligne):
	donneesTrame=[]
 
	donneesTrame.append("type=I")

	for i in range(16,len(ligne)):

		if (ligne[i] == "U"):
			#2 chiffres, valeurs : 0x00 à 0x96 (décimal: 0,0 à 15,0)
			tensionBatterie = ligne[i+1:i+3]
			tensionBatterieDec = int(tensionBatterie, 16)
			#pour nombre à virgule
			tensionBatterieDec = truediv(tensionBatterieDec,10)
			donneesTrame.append("vbat="+str(tensionBatterieDec))

		if (ligne[i] == "T"):
			#3 chiffres, valeurs : 
			#nombre positif : 0x000 à 0x320 (décimal: 0,0 à 80,0°)
			#nombre négatif : 0xFFF à 0xE6F (décimal: -1,0 à -40,0°)
			temperature = ligne[i+1:i+4]
			temperatureDec = int(temperature, 16)
			print 'temp decimal : ' + str(temperatureDec)
			#gestion nombre négatif :
			if(3695<=temperatureDec<=4095):
				temperatureDec=temperatureDec-4096;
			temperatureDec = truediv(temperatureDec,10)
			print 'temp division par 10 : ' + str(temperatureDec)
			donneesTrame.append("temp_capteur="+str(temperatureDec))

		if (ligne[i] == "H"):
			#2 chiffres, valeurs : 0x00 à 0x64 (décimal: 0 à 100%)
			hygrometrie = ligne[i+1:i+3]
			hygrometrieDec = int(hygrometrie, 16)
			donneesTrame.append("hygro_capteur="+str(hygrometrieDec))

		if (ligne[i] == "M"):
			#2 chiffres, valeurs : 
			#nombre positif : 0x00 à 0x7D (décimal: 0 à 125°)
			#nombre négatif : 0xFF à 0xD8 (décimal: -1 à -40°)
			temperatureBalance = ligne[i+1:i+3]
			temperatureBalanceDec = int(temperatureBalance, 16)
			#print 'temp decimal : ' + str(temperatureBalanceDec)
			#gestion nombre négatif :
			if(216<=temperatureBalanceDec<=255):
				temperatureBalanceDec=temperatureBalanceDec-256;
			temperatureBalanceDec = truediv(temperatureBalanceDec,10)
			print 'temp division par 10 : ' + str(temperatureBalanceDec)
			donneesTrame.append("temp_balance="+str(temperatureBalanceDec))

		if (ligne[i] == "V"):
			#3 chiffres, valeurs : 0x032 à 0x3E8 (décimal: 50 à 1000)
			vibration = ligne[i+1:i+4]
			vibrationDec = int(vibration, 16)
			donneesTrame.append("vib="+str(vibrationDec))

		if (ligne[i] == "G"):
			#3 chiffres, valeurs : 0x190 à 0x7D0 (décimal: 400 à 2000)
			tauxCO2 = ligne[i+1:i+4]
			tauxCO2Dec = int(tauxCO2, 16)
			donneesTrame.append("co2="+str(tauxCO2Dec))

		if (ligne[i] == "N"):
			#1 chiffres, valeurs : 0x1 à 0x9 (décimal: 1 à 9)
			nour = ligne[i+1:i+2]
			nour = int(nour, 16)
			donneesTrame.append("nour="+str(nour))

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame

def Decoupage_Trame_RucherExterne(ligne):
	donneesTrame=[]
 
	donneesTrame.append("type=E")

	for i in range(16,len(ligne)):

		if (ligne[i] == "P"):
			#3 chiffres, valeurs : 0x000 à 0x3E8 (décimal: 0.0 à 100.0)
			masseBalance = ligne[i+1:i+4]
			masseBalance = int(masseBalance, 16)
			masseBalance = truediv(masseBalance,10)
			donneesTrame.append("masse="+str(masseBalance))

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame

def Def_Trame_PHP(adresseMac,donneesTrame):
	print donneesTrame
	date=datetime.datetime.now()
	requetePHP=pathSiteWeb+"script_gateway.php?"+"mac="+adresseMac+"&date="+str(date.date())+"&heure="+str(date.time())

	#construction de la trame PHP avec les données recues
	for data in donneesTrame:
		requetePHP+="&"+data

	#print requetePHP
	File_WriteLog(pathLog, 6, requetePHP)
	return requetePHP

def Gestion_Trame(ligne):
	File_WriteLog(pathLog, 5, ligne)
	typeEmetteur = ligne[0:2]

	if typeEmetteur == "01" :
		adresseMac = ligne[2:15]
		donneesTrame=Decoupage_Trame_Station(ligne)
		requetePHP=Def_Trame_PHP(adresseMac,donneesTrame)
	elif typeEmetteur == "02" :
		adresseMacRucheInterne = ligne[2:14]
		adresseMacRucheExterne = ligne[16:28]
		donneesTrameRucheInterne =Decoupage_Trame_RucherInterne(ligne)
		requetePHP_RucheInterne =Def_Trame_PHP(adresseMacRucheInterne,donneesTrameRucheInterne)
		donneesTrameRucheExterne =Decoupage_Trame_RucherExterne(ligne)
		requetePHP_RucheExterne =Def_Trame_PHP(adresseMacRucheExterne,donneesTrameRucheExterne)
	elif typeEmetteur == "03" :
		adresseMacRucheExterne  = ligne[2:14]
		adresseMacRucheInterne  = ligne[16:28]
		donneesTrameRucheExterne=Decoupage_Trame_RucherExterne(ligne)
		requetePHP_RucheExterne=Def_Trame_PHP(adresseMacRucheExterne,donneesTrameRucheExterne)
		donneesTrameRucheInterne=Decoupage_Trame_RucherInterne(ligne)
		requetePHP_RucheInterne=Def_Trame_PHP(adresseMacRucheInterne,donneesTrameRucheInterne)

	gestionErreur = ligne[14:16]

	fichier.close()

#main
fichier=File_Open(path)
ligneLue=File_Read(fichier)
Gestion_Trame(ligneLue)
File_Erase(path)
File_WriteLog(pathLog, 4, DataEmpty)
Ack()
File_Close(fichier)
