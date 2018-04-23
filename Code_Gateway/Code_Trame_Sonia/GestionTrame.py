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
from FichierGestion import *

#constantes
path="trameExemple.txt"
pathLog="log.txt"
DataEmpty=""
pathSiteWeb="http://wwww.xxx.xxx/"
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

		if (ligne[i] == "B"):
			tensionBatterie = ligne[i+1:i+3]
			tensionBatterieDec = int(tensionBatterie, 16)
			tensionBatterieDec = truediv(tensionBatterieDec,10)
			donneesTrame.append("vbat="+str(tensionBatterieDec))

		if (ligne[i] == "S"):
			solaire = ligne[i+1:i+3]
			solaireDec = int(solaire, 16) #conversion hexa en decimal
			solaireDec = solaireDec + offsetSolaire
			donneesTrame.append("sol="+str(solaireDec))

		if (ligne[i] == "T"):
			temperature = ligne[i+1:i+5]
			temperatureDec = int(temperature, 16)
			temperatureDec = truediv(temperatureDec,10)
			donneesTrame.append("temp_capteur="+str(temperatureDec))

		if (ligne[i] == "H"):
			hygrometrie = ligne[i+1:i+3]
			hygrometrieDec = int(hygrometrie, 16)
			donneesTrame.append("hygro_capteur="+str(hygrometrieDec))

		if (ligne[i] == "E"):
			pluviometrie = ligne[i+1:i+3]
			pluviometrieDec = int(pluviometrie, 16)
			pluviometrieDec = pluviometrieDec*impulsionPluviometrie
			donneesTrame.append("pluvio="+str(pluviometrieDec))

		if (ligne[i] == "V"):
			anemometre = ligne[i+1:i+4]
			anemometreDec = int(anemometre, 16)
			donneesTrame.append("vent="+str(anemometreDec))

		if (ligne[i] == "P"):
			pression = ligne[i+1:i+5]
			pressionDec = int(pression, 16)
			pressionDec = pressionDec + offsetPression
			donneesTrame.append("pres="+str(pressionDec))

		if (ligne[i] == "D"):
			directionVent = ligne[i+1:i+2]
			directionVentDec = int(directionVent, 16)
			directionVentDec = ConversionDirectionVent(directionVentDec)
			print directionVentDec
			donneesTrame.append("dirv="+str(directionVentDec))

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame

def Decoupage_Trame_RucherInterne(ligne):
	donneesTrame=[]
 
	donneesTrame.append("type=I")

	for i in range(16,len(ligne)):

		if (ligne[i] == "B"):
			tensionBatterie = ligne[i+1:i+3]
			tensionBatterieDec = int(tensionBatterie, 16)
			tensionBatterieDec = truediv(tensionBatterieDec,10)
			donneesTrame.append("vbat="+str(tensionBatterieDec))

		if (ligne[i] == "T"):
			temperature = ligne[i+1:i+5]
			temperatureDec = int(temperature, 16)
			temperatureDec = truediv(temperatureDec,10)
			donneesTrame.append("temp_capteur="+str(temperatureDec))

		if (ligne[i] == "H"):
			hygrometrie = ligne[i+1:i+3]
			hygrometrieDec = int(hygrometrie, 16)
			donneesTrame.append("hygro_capteur="+str(hygrometrieDec))

		if (ligne[i] == "M"):
			temperatureBalance = ligne[i+1:i+3]
			temperatureBalanceDec = int(temperatureBalance, 16)
			donneesTrame.append("temp_balance="+str(temperatureBalanceDec))

		if (ligne[i] == "V"):
			vibration = ligne[i+1:i+3]
			vibrationDec = int(vibration, 16)
			donneesTrame.append("vib="+str(vibrationDec))

		if (ligne[i] == "C"):
			tauxCO2 = ligne[i+1:i+5]
			tauxCO2Dec = int(tauxCO2, 16)
			donneesTrame.append("co2="+str(tauxCO2Dec))

		if (ligne[i] == "N"):
			nour = ligne[i+1:i+3]
			nour = int(nour, 16)
			donneesTrame.append("nour="+str(nour))

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame

def Decoupage_Trame_RucherExterne(ligne):
	donneesTrame=[]
 
	donneesTrame.append("type=E")

	for i in range(16,len(ligne)):

		if (ligne[i] == "P"):
			masseBalance = ligne[i+1:i+3]
			masseBalance = int(masseBalance, 16)
			donneesTrame.append("masse="+str(masseBalance))

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame

def Def_Trame_PHP(adresseMac,donneesTrame):
	print donneesTrame
	date=datetime.datetime.now()
	requetePHP=pathSiteWeb+"add.php?"+"mac="+adresseMac+"&date="+str(date.date())+"&heure="+str(date.time())

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
File_Close(fichier)
