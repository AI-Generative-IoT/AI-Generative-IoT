##################################################################################################################################################################
#                                                                                                                                                                #
#   Autoren: Adrian Dahl und Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                                                #
##################################################################################################################################################################

# PYTHON ROUTINE zur Verschlüsselung von E-Mails durch ein GAN-basiertes künstliches neuronales Netzwerk #
# Allgemein: Es wurde in dieser aktuellesten Version eine Invertierende Schaltung verwendet - siehe Funktions-Definition unter CNOT.

import os
import sys
import statistics

import math
import random
import unicodedata

import time

start_time = time.time()

# Definition von Funktionen zur Verschlüsselung a kongruent b mod 52 durch GAN

def letters_to_value(x): # Definiere eine Funktion zur Abbildung von Buchstaben auf Zahlen a kongruent b mod 52 (bzw. eine höhere Anzahl von Buchstaben)

    x_value = 0

    unicode_letters = [chr(i) for i in range(0x110000) if unicodedata.category(chr(i)).startswith('L')]

    for k in range(len(unicode_letters)):

        if (x == unicode_letters[k]):
            
            x_value = k

    return x_value

def value_to_letters(x): # Definiere eine Funktion zur Abbildung von Zahlen auf Buchstaben a kongruent b mod 52 (bzw. eine höhere Anzahl von Buchstaben)

    x_value = ''

    unicode_letters = [chr(i) for i in range(0x110000) if unicodedata.category(chr(i)).startswith('L')]

    for k in range(len(unicode_letters)):

        if (x == k):
            
            x_value = unicode_letters[k]

    return x_value

# Definition von Funktionen zur Verschlüsselung b kongruent a mod 52 durch GAN

def Generator(length, input_key, train):

    output_key = [0]*length

    for j in range(0, length): # Generiere einen zufälligen binären Schlüssel zum Abgleich mit dem Referenzschlüssel

        output_key[j] = random.randint(0,1)

    return(output_key)
    
def Diskriminator(length, input_key, ideal_key):

    difference = [0]*length

    for j in range(0, length):

        difference[j] = math.fabs(ideal_key[j] - input_key[j]) # Berechne die Abweichung zwischen Referenzschlüssel und dynamisch generiertem Schlüssel

    return(difference)

def NOT(length, input_key): # Definiert ein NOT-Gate

    output_key = [0]*length

    with open("config.txt", 'w') as file: # Importiere den Zeichenstring aus dem externen File mit Bezeichnung EMailString.txt

        for k in range(0, length):

            m = random.randint(0, 1)

            if (input_key[m] == 0): input_key[m] = 1        
            else: input_key[m] = 0
      
            output_key[k] = input_key[k]

            file.write(str(m)+',')
        
        return output_key

def CNOT(length, input_key): # Definiert eine paarweise Invertierung der Ausgangskonfiguration

    output_key = [0]*length
        
    for k in range(0, length):

        if (input_key[k] == 0): input_key[k] = 1
        else: input_key[k] = 0

    output_key[k] = input_key[k]

def OR(length, input_key): # Definiert ein OR-Gate

    output_key = [0]*length
        
    for k in range(1, M):

        if (k == 8 or k == 6 or k == 4 or k == 2):
        
            if (input_key[k] == 0 and input_key[k-1] == 0): input_key[k-1] = 0
            if (input_key[k] == 0 and input_key[k-1] == 1): input_key[k-1] = 1        
            if (input_key[k] == 1 and input_key[k-1] == 0): input_key[k-1] = 1
            if (input_key[k] == 1 and input_key[k-1] == 1): input_key[k-1] = 1
              
    for k in range(0, M):

        output_key[k] = input_key[k]
        
    return output_key
        
def AND(length, input_key): # Definiert ein AND-Gate

    output_key = [0]*length
        
    for k in range(1, M):

        if (k == 8 or k == 6 or k == 4 or k == 2): 
  
            if (input_key[k] == 0 and input_key[k-1] == 0): input_key[k-1] = 0
            if (input_key[k] == 0 and input_key[k-1] == 1): input_key[k-1] = 0        
            if (input_key[k] == 1 and input_key[k-1] == 0): input_key[k-1] = 0
            if (input_key[k] == 1 and input_key[k-1] == 1): input_key[k-1] = 1
              
    for k in range(0, M):

        output_key[k] = input_key[k]
        
    return output_key

def XOR(length, input_key): # Definiert ein XOR-Gate ==> CNOT

    output_key = [0]*length
        
    for k in range(1, M):

        if (k == 8 or k == 6 or k == 4 or k == 2):

            if (input_key[k] == 0 and input_key[k-1] == 0): input_key[k-1] = 0
            if (input_key[k] == 0 and input_key[k-1] == 1): input_key[k-1] = 1        
            if (input_key[k] == 1 and input_key[k-1] == 0): input_key[k-1] = 1
            if (input_key[k] == 1 and input_key[k-1] == 1): input_key[k-1] = 0
              
    for k in range(0, M):

        output_key[k] = input_key[k]
        
    return output_key

def NAND(length, input_key): # Definiert ein NAND-Gate

    output_key = [0]*length
        
    for k in range(1, M):

        if (k == 8 or k == 6 or k == 4 or k == 2):
        
            if (input_key[k] == 0 and input_key[k-1] == 0): input_key[k-1] = 1
            if (input_key[k] == 0 and input_key[k-1] == 1): input_key[k-1] = 1        
            if (input_key[k] == 1 and input_key[k-1] == 0): input_key[k-1] = 1
            if (input_key[k] == 1 and input_key[k-1] == 1): input_key[k-1] = 0
              
    for k in range(0, M):

        output_key[k] = input_key[k]
        
    return output_key

def NOR(length, input_key): # Definiert ein NOR-Gate

    output_key = [0]*length
        
    for k in range(1, M):

        if (k == 8 or k == 6 or k == 4 or k == 2):
        
            if (input_key[k] == 0 and input_key[k-1] == 0): input_key[k-1] = 1
            if (input_key[k] == 0 and input_key[k-1] == 1): input_key[k-1] = 0        
            if (input_key[k] == 1 and input_key[k-1] == 0): input_key[k-1] = 0
            if (input_key[k] == 1 and input_key[k-1] == 1): input_key[k-1] = 0
              
    for k in range(0, M):

        output_key[k] = input_key[k]
                
    return output_key

def GAN(length, initial_key, reference_key):

    k = 0
    GAN_Key = [0]*length # Definiere den GAN-Schlüssel mit der Variable GAN_Key als Pythonliste mit der gleichen Anzahl von Elementen wie die anderen Keys 
        
    while(True):

        sum = 0.0
        initial_key = CNOT(length, initial_key)

        if (k == 0): L = Generator(length, initial_key, reference_key) 

        if (k > 0): 

            GAN_Key = Generator(length, L, M)
            initial_key = GAN_Key
            L = CNOT(length, GAN_Key)
        
        M = Diskriminator(length, L, reference_key)

        for j in range(0, length):

            sum = sum + math.fabs(M[j])

        k = k + 1

        if (sum == float(length)): # Hier wird die Genaugkeit an das GAN festgelegt.

            return(initial_key)
            break

def GenerateReferenceKey(keysize):

    for j in range(0, keysize): # Generiere einen zufälligen binären Schlüssel als Referenzwert (entspricht externem und unbekanntem Referenzwert)

        R[j] = random.randint(0,1)
    
    return R
    
def GenerateInitialKey(keysize):

    for j in range(0, keysize): # Generiere einen zufälligen binären Schlüssel als Startwert

        K[j] = random.randint(0,1)

    return K

# Definiere eine Pythonliste mit Elementen aus dem deutschen Alphabet

with open("EMailString.txt") as file: # Importiere den Zeichenstring aus dem externen File mit Bezeichnung EMailString.txt

    S = file.read()
    
M = 6 # Länge des Schlüssels in Einheiten von Bits

K = ['']*M # Definiere den Schlüssel K als Pythonliste mit der gleichen Anzahl von Elementen wie S     
R = ['']*M # Definiere den Schlüssel R als Pythonliste mit der gleichen Anzahl von Elementen wie S  

fS = ['']*len(S) # Definiere eine Python Liste für den kodierten Zeichenstring als verschlüsselte Zahlenfolge
fSS = '' # Definiere eine Python Liste für den dekodierten Zeichenstring als entschlüsselte Zahlenfolge

rkey = []
dkey = []
ARR_Keys = []

dvalue = 0.0
print('Number of Key Elements : ', len(S))

alphabet = [chr(i) for i in range(0x110000) if unicodedata.category(chr(i)).startswith('L')]

for k in range(0, len(S)):

    print('Generate Key Element Nr. ', k)

    K = GenerateInitialKey(M) # Generiere den ersten Schlüssel als Startwert für das GAN
    R = GenerateReferenceKey(M) # Generiere einen Referenzschlüssel (anfangs dengleichen Keywert)

    rkey.append(R.copy())

    K = R.copy() # Lege eine Anfangsbedingung mit K = R fest     

    ARR_Keys = ARR_Keys + R # Speichere jeweils den Referenzkey, der modulu CNOT den Key K erzeugt
    key = GAN(M, K, R) # Modelliere ein GAN-Netzwerk zur Rekonstruktion eines der möglichen Eingangssignale (bisher unbekannt)

    dvalue = 0.0

    for l in range(0, len(key)):

        dvalue = dvalue + 2**l*key[l]
    
    dkey.append(int(dvalue))

# Binär-zu-Dezimalkonverter einfügen
# Schleife über unterschiedliche Binärkeys zur Generierung eines dezimalen Schlüssels aus mehreren Komponenten #

for i in range(0,len(S)): # Verschlüsselung der Textzeichen durch den übertragenen Zahlencodes 

    if (S[i] != ' '): fS[i] = (letters_to_value(S[i]) + dkey[i]) % len(alphabet) # Kongruent mod 52
    else: fS[i] = -1

with open("EMailStringOut.txt", 'w') as file: # Importiere den Zeichenstring aus dem externen File mit Bezeichnung EMailString.txt

    for k in range(0, len(fS)):

        file.write(str(fS[k]) + '\n')

with open("ReferenceKeys.txt", 'w') as file: # Importiere den Zeichenstring aus dem externen File mit Bezeichnung EMailString.txt

    for k in range(0, len(rkey)):

        file.write(str(rkey[k]) + '\n')
    
end_time = time.time()

print({end_time - start_time})