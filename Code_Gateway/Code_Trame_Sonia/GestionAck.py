#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Auteur : SJ
Date : 22/01/18
Fonction : fonctions permettant de renvoyer un accusé de reception
"""

import os
import time
import datetime
from GestionFichier import *

path="trameExempleAck.txt"
pathLog="log.txt"

def Ack():
	fichier=File_Open(path)
	ligneLue=File_Read(fichier)
	#parcours ligne
	for i in range(0,len(ligneLue)):
		#code erreur : 
		#G00 : OK données enregistrées
		#GFF : NOK erreur
		if (ligneLue[i] == "G"):
			codeErreur = ligneLue[i+1:i+3]
			if (codeErreur=="00"):
				print "OK"
				File_WriteLog(pathLog, 7, "")
			if (codeErreur=="FF"):
				print "NOK"
				File_WriteLog(pathLog, 8, "")
	
	File_Erase(path)
	File_Close(fichier)
