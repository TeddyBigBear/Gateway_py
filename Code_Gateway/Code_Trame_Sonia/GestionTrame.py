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
path="/Users/utilisateur/Documents/Polytech_EII_3/Projet Elec/CodesPython/trameExemple.txt"
pathLog="/Users/utilisateur/Documents/Polytech_EII_3/Projet Elec/CodesPython/log.txt"
DataEmpty=""
pathSiteWeb="http://wwww.xxx.xxx/"
requetePHP=""

#fonctions
def Decoupage_Trame_Station(ligne):
	offsetPression = 800
	offsetSolaire = 120000
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
			donneesTrame.append("hygro="+str(hygrometrieDec))

		if (ligne[i] == "E"):
			pluviometrie = ligne[i+1:i+3]
			pluviometrieDec = int(pluviometrie, 16)
			donneesTrame.append("pluvio="+str(pluviometrieDec))

		if (ligne[i] == "V"):
			anemometre = ligne[i+1:i+3]
			anemometreDec = int(anemometre, 16)
			donneesTrame.append("vent="+str(anemometreDec))

		if (ligne[i] == "P"):
			pression = ligne[i+1:i+5]
			pressionDec = int(pression, 16)
			pressionDec = pressionDec + offsetPression
			donneesTrame.append("pres="+str(pressionDec))

		if (ligne[i] == "D"):
			directionVent = ligne[i+1:i+3]
			directionVentDec = int(directionVent, 16)
			donneesTrame.append("dirv="+str(directionVentDec))

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame
	#print tensionBatterieDec

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
			donneesTrame.append("hygro="+str(hygrometrieDec))

		if (ligne[i] == "P"):
			masseBalance = ligne[i+1:i+3]
			masseBalance = int(masseBalance, 16)
			donneesTrame.append("masse="+str(masseBalance))

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

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame
	#print tensionBatterieDec

def Decoupage_Trame_RucherExterne(ligne):
	donneesTrame=[]
 
	donneesTrame.append("type=E")

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
			donneesTrame.append("hygro="+str(hygrometrieDec))

		if (ligne[i] == "P"):
			masseBalance = ligne[i+1:i+3]
			masseBalance = int(masseBalance, 16)
			donneesTrame.append("masse="+str(masseBalance))

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

	File_WriteLog(pathLog, 2, DataEmpty)
	return donneesTrame
	#print tensionBatterieDec

def Def_Trame_PHP(adresseMac,typeEmmetteur,donneesTrame):
	print donneesTrame
	date=datetime.datetime.now()
	requetePHP=pathSiteWeb+"add.php?"+"mac="+adresseMac+"&date="+str(date.date())+"&heure="+str(date.time())

	for data in donneesTrame:
		requetePHP+="&"+data

	#print requetePHP
	File_WriteLog(pathLog, 6, requetePHP)
	return requetePHP

def Gestion_Trame(ligne):
	adresseMac = ligne[0:12]
	typeEmetteur = ligne[12:14]
	gestionErreur = ligne[14:16]

	File_WriteLog(pathLog, 5, ligne)

	if typeEmetteur == "01" :
		donneesTrame=Decoupage_Trame_Station(ligne)
	elif typeEmetteur == "02" :
		donneesTrame=Decoupage_Trame_RucherInterne(ligne)
	elif typeEmetteur == "03" :
		donneesTrame=Decoupage_Trame_RucherExterne(ligne)

	requetePHP=Def_Trame_PHP(adresseMac,typeEmetteur,donneesTrame)
	print requetePHP

	fichier.close()


#main
fichier=File_Open(path)
ligneLue=File_Read(fichier)
Gestion_Trame(ligneLue)
File_Erase(path)
File_WriteLog(pathLog, 4, DataEmpty)
File_Close(fichier)
