# PYTHON ROUTINE zur Verschlüsselung von E-Mails durch ein GAN-basiertes künstliches neuronales Netzwerk #

import os
import sys
import math
import random
import statistics

def Generator(length, input_key, train):
    output_key = [0] * length
    for j in range(0, length):  # Generiere einen zufälligen binären Schlüssel
        if (train[j] != 0.00):
            output_key[j] = random.randint(0, 1)
        else:
            output_key[j] = input_key[j]
    return (output_key)

def Diskriminator(length, input_key, ideal_key):
    difference = [0.0] * length
    for j in range(0, length):
        difference[j] = math.fabs(ideal_key[j] - input_key[j])
    return (difference)


def CNOT(length, input_key):
    output_key = input_key

    for m in range(0, length):
        # if (input_key[m] == 1 and input_key[m - 1] == 0): input_key[m - 1] = 1
        # elif (input_key[m] == 1 and input_key[m - 1] == 1): input_key[m - 1] = 0
        if input_key[m] == 1:
            output_key[m - 1] = (input_key[m-1] + 1) % 2
    return output_key


def GAN(length, initial_key, reference_key):
    i = 0
    GAN_Key = [1] * length  # Definiere den GAN-Schlüssel GAN_Key als Pythonliste mit der gleichen Anzahl von Elementen wie die anderen Keys

    while (True):
        sum = 0.0
        initial_key = CNOT(length, initial_key)
        if (i == 0):
            L = Generator(length, initial_key, GAN_Key)
        else:
            L = CNOT(length, Generator(length, L, D))  # Bemerkung: Hier hat noch die CNOT-Funktion gefehlt.
        i += 1
        D = Diskriminator(length, L, reference_key)
        for j in range(0, length):
            sum = sum + D[j]
        if (sum == 0):
           return (GAN_Key)
        else:
           GAN_Key = L

def GenerateInitialKey(keysize):
    for j in range(0, keysize):  # Generiere einen zufälligen binären Schlüssel als Initialwert
        KI[j] = random.randint(0, 1)
    return KI

def GenerateReferenceKey(keysize):
    for j in range(0, keysize):  # Generiere einen zufälligen binären Schlüssel als Referenzwert (entspricht externem und unbekanntem Referenzwert)
        KR[j] = random.randint(0, 1)
    return KR

####################################################################################################################################################

with open("EMailString.txt", 'r', encoding = 'utf-8') as file:  # Importiere den Zeichenstring aus dem externen File mit Bezeichnung EMailString.txt
    S = file.read()
print('Number of Key Elements: ', len(S))  # Zeichenzahl Text

M = 8  # Länge des Schlüssels in Einheiten von Bits
KI = ['']*M  # Definiere den Initialschlüssel KI als Pythonliste
KR = ['']*M  # Definiere den Referenzschlüssel KR als Pythonliste
I = ['']*M  # Definiere den Schlüssel I als Pythonliste
R = [''] * M  # Definiere den Schlüssel R als Pythonliste
dkey = []

for k in range(0, len(S)):
    I = GenerateInitialKey(M)  # Generiere den ersten Schlüssel als Startwert für das GAN
    R = GenerateReferenceKey(M)  # Generiere einen Referenzschlüssel
    key = GAN(M, I, R) # Modelliere ein GAN-Netzwerk zur Rekonstruktion eines möglichen Eingangssignales
    dvalue = 0
    for j in range(0, M):
        dvalue = dvalue + 2**j*key[j]
    dkey.append(dvalue)  # wichtiger Schlüssel für die Ver- unt irreversible Entschlüsselung

# Binär-zu-Dezimalkonverter einfügen #
# Schleife über unterschiedliche Binärkeys zur Generierung eines dezimalen Schlüssels aus mehreren Komponenten #
la = 256 # ASCII-Code Dezimalwert 0 bis 255
fS = ['']*len(S)  # Definiere eine Python Liste für den kodierten Zeichenstring als verschlüsselte Zahlenfolge
for i in range(0, len(S)):  # Verschlüsselung von E-Mails durch den übertragene Zahlencodes
    su = (ord(S[i]) + dkey[i]) % la  # Kennzahl zur Verschlüsselung der Textzeichen
    t = 0
    for j in range(0, la):  # sucht Zeichen
        if ord(S[i]) == j:
            fS[i] =  su
            t = 1
            break
    if ord(S[i]) == 8364 or ord(S[i]) == 8240:  # Zeichen € und ‰
        fS[i] = su
        t = 1
    if t == 0:
        print('unbekanntes Zeichen: ' + S[i])
        fS[i] = (ord('*') + dkey[i]) % la

print('Verschlüsselte E-Mail: ', fS)

with open("Schlüssel.txt", 'w') as datei:  # Datei mit verschlüsseltem Text und Schlüssel dkey
    datei.write(str((len(S)*2 + 27)) + ' ')  # Anzahl Zeichen im Text verschlüsselt

    for i in range(0, len(fS)):  # fS in Datei
        datei.write(str(fS[i]) + ' ')
    datei.write('\n')
    for i in range(0, len(dkey)):  # dkey in datei
        datei.write(str(dkey[i]) + ' ')
    datei.write('\n')
