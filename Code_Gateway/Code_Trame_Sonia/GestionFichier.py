#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Auteur : SJ
Date : 22/01/18
Fonction : fonctions permettant d'ouvrir, d'écrire et de lire dans un fichier
"""

import os
import time
import datetime

def File_Exist(fichier):
	try:
		file(fichier)
		return True
   	except:
   		return False

def File_Open(path):
	#verification que le fichier existe sinon création du fichier
	#if not os.path.isfile(path):
	fichier = open(path, "r")
	return fichier
	#fichier.close()

#pas utilisé encore
def File_Write(path):
	with open(path, "a") as fichier:
		print fichier.write("\ntest ")

def File_WriteLog(path, code, data):
	#ecriture en mode ajout
	with open(path, "a") as fichier:
		print fichier.write(str(datetime.datetime.now())+" : ")

		if (code == 1):
			print fichier.write("Trame LoRa recue\n")
		elif (code == 2):
			print fichier.write("Decoupage OK\n")
		elif (code == 3):
			print fichier.write("Envoi de la requete PHP\n")
		elif (code == 4):
			print fichier.write("Trame supprimée du buffer\n")
		elif (code == 5):
			print fichier.write("Trame SPI : " + data +"\n")
		elif (code == 6):
			print fichier.write("Trame PHP : " + data +"\n")
		elif (code == 7):
			print fichier.write("Données enregistrées sur le serveur. \n")
		elif (code == 8):
			print fichier.write("!!!!!! Erreur : données non enregistrées sur le serveur !!!!!! \n")

def File_Read(fichier):
	ligneLue = fichier.readline()
	#lignes = fichier.readlines()
	#for i in fichier.readlines() :
		#lignes = fichier.readlines()
		#print lignes[i]
	return ligneLue

def File_Close(fichier):
	fichier.close()

def File_Erase(path):
	#on récupère toutes les données avant de les écraser
	fichier = open(path, "r")
	lignes = fichier.readlines()
	fichier.close()

	#ecrasement des données et réécriture des données sans la 1ere ligne
	with open(path, "w") as fichier:
		for i in range(1,len(lignes)):
			fichier.write(lignes[i])
	print "Effacement de la 1ere ligne effectuée"
