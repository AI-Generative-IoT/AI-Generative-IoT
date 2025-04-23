#####################################################################################################################################################################
#                                                                                                                                                                   #
#   Autoren: Renars Miculis und Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                                                   #
#####################################################################################################################################################################

# PYTHON ROUTINE zur Verschlüsselung von E-Mails durch ein GAN-basiertes künstliches neuronales Netzwerk #
# Allgemein: Es wurde in dieser aktuellesten Version eine Invertierende Schaltung verwendet - siehe Funktions-Definition unter CNOT.

import os
import sys
import statistics
import math
import random

# Definition von Funktionen zur Verschlüsselung a kongruent b mod 52 durch GAN

def letters_to_value(x): # Definiere eine Funktion zur Abbildung von Buchstaben auf Zahlen a kongruent b mod 52 (bzw. eine höhere Anzahl von Buchstaben)
    
    x_value = 0

    if (x == 'a') : x_value = 0
    if (x == 'b') : x_value = 1
    if (x == 'c') : x_value = 2
    if (x == 'd') : x_value = 3
    if (x == 'e') : x_value = 4
    if (x == 'f') : x_value = 5
    if (x == 'g') : x_value = 6
    if (x == 'h') : x_value = 7
    if (x == 'i') : x_value = 8
    if (x == 'j') : x_value = 9
    if (x == 'k') : x_value = 10
    if (x == 'l') : x_value = 11
    if (x == 'm') : x_value = 12
    if (x == 'n') : x_value = 13
    if (x == 'o') : x_value = 14
    if (x == 'p') : x_value = 15
    if (x == 'q') : x_value = 16
    if (x == 'r') : x_value = 17
    if (x == 's') : x_value = 18
    if (x == 't') : x_value = 19
    if (x == 'u') : x_value = 20
    if (x == 'v') : x_value = 21
    if (x == 'w') : x_value = 22
    if (x == 'x') : x_value = 23
    if (x == 'y') : x_value = 24
    if (x == 'z') : x_value = 25

    if (x == 'A') : x_value = 26
    if (x == 'B') : x_value = 27
    if (x == 'C') : x_value = 28
    if (x == 'D') : x_value = 29
    if (x == 'E') : x_value = 30
    if (x == 'F') : x_value = 31
    if (x == 'G') : x_value = 32
    if (x == 'H') : x_value = 33
    if (x == 'I') : x_value = 34
    if (x == 'J') : x_value = 35
    if (x == 'K') : x_value = 36
    if (x == 'L') : x_value = 37
    if (x == 'M') : x_value = 38
    if (x == 'N') : x_value = 39
    if (x == 'O') : x_value = 40
    if (x == 'P') : x_value = 41
    if (x == 'Q') : x_value = 42
    if (x == 'R') : x_value = 43
    if (x == 'S') : x_value = 44
    if (x == 'T') : x_value = 45
    if (x == 'U') : x_value = 46
    if (x == 'V') : x_value = 47
    if (x == 'W') : x_value = 48
    if (x == 'X') : x_value = 49
    if (x == 'Y') : x_value = 50
    if (x == 'Z') : x_value = 51
    if (x == '.') : x_value = 52

    return x_value

def value_to_letters(x): # Definiere eine Funktion zur Abbildung von Zahlen auf Buchstaben a kongruent b mod 52 (bzw. eine höhere Anzahl von Buchstaben)
     
    x_value = ''

    if (x == 0) : x_value = 'a'
    if (x == 1) : x_value = 'b'
    if (x == 2) : x_value = 'c'
    if (x == 3) : x_value = 'd'
    if (x == 4) : x_value = 'e'
    if (x == 5) : x_value = 'f'
    if (x == 6) : x_value = 'g'
    if (x == 7) : x_value = 'h'
    if (x == 8) : x_value = 'i'
    if (x == 9) : x_value = 'j'
    if (x == 10) : x_value = 'k'
    if (x == 11) : x_value = 'l'
    if (x == 12) : x_value = 'm'
    if (x == 13) : x_value = 'n'
    if (x == 14) : x_value = 'o'
    if (x == 15) : x_value = 'p'
    if (x == 16) : x_value = 'q'
    if (x == 17) : x_value = 'r'
    if (x == 18) : x_value = 's'
    if (x == 19) : x_value = 't'
    if (x == 20) : x_value = 'u'
    if (x == 21) : x_value = 'v'
    if (x == 22) : x_value = 'w'
    if (x == 23) : x_value = 'x'
    if (x == 24) : x_value = 'y'
    if (x == 25) : x_value = 'z'
    
    if (x == 26) : x_value = 'A'
    if (x == 27) : x_value = 'B'
    if (x == 28) : x_value = 'C'
    if (x == 29) : x_value = 'D'
    if (x == 30) : x_value = 'E'
    if (x == 31) : x_value = 'F'
    if (x == 32) : x_value = 'G'
    if (x == 33) : x_value = 'H'
    if (x == 34) : x_value = 'I'
    if (x == 35) : x_value = 'J'
    if (x == 36) : x_value = 'K'
    if (x == 37) : x_value = 'L'
    if (x == 38) : x_value = 'M'
    if (x == 39) : x_value = 'N'
    if (x == 40) : x_value = 'O'
    if (x == 41) : x_value = 'P'
    if (x == 42) : x_value = 'Q'
    if (x == 43) : x_value = 'R'
    if (x == 44) : x_value = 'S'
    if (x == 45) : x_value = 'T'
    if (x == 46) : x_value = 'U'
    if (x == 47) : x_value = 'V'
    if (x == 48) : x_value = 'W'
    if (x == 49) : x_value = 'X'
    if (x == 50) : x_value = 'Y'
    if (x == 51) : x_value = 'Z'
    if (x == 52) : x_value = '.'

    return x_value

# Definition von Funktionen zur Verschlüsselung b kongruent a mod 52 durch GAN

def strings_to_value(x): # Definiere eine Funktion zur Abbildung von Strings auf Zahlen a kongruent b mod 52
    
    x_value = 0

    if (x == '0') : x_value = 0
    if (x == '1') : x_value = 1
    if (x == '2') : x_value = 2
    if (x == '3') : x_value = 3
    if (x == '4') : x_value = 4
    if (x == '5') : x_value = 5
    if (x == '6') : x_value = 6
    if (x == '7') : x_value = 7
    if (x == '8') : x_value = 8
    if (x == '9') : x_value = 9
    
    return x_value

def value_to_strings(x): # Definiere eine Funktion zur Abbildung von Zahlen auf Strings a kongruent b mod 52
     
    x_value = ''

    if (x == 0) : x_value = '0'
    if (x == 1) : x_value = '1'
    if (x == 2) : x_value = '2'
    if (x == 3) : x_value = '3'
    if (x == 4) : x_value = '4'
    if (x == 5) : x_value = '5'
    if (x == 6) : x_value = '6'
    if (x == 7) : x_value = '7'
    if (x == 8) : x_value = '8'
    if (x == 9) : x_value = '9'

    return x_value

def Generator(length, input_key, train):

    output_key = [0]*length

    for j in range(0, length): # Generiere einen zufälligen binären Schlüssel zum Abgleich mit dem Referenzschlüssel
        
    # Train-Funktion nutzt IF-Kontrollstruktur
    # if (input_key[j] != output_key[j]): output_key[j] = random.randint(0,1) 
    
        output_key[j] = random.randint(0,1)
    
    return(output_key)
    
def Diskriminator(length, input_key, ideal_key):

    difference = [0]*length

    for j in range(0, length):

        difference[j] = math.fabs(ideal_key[j] - input_key[j]) # Berechne die Abweichung zwischen Referenzschlüssel und dynamisch generiertem Schlüssel

    return(difference)

def CNOT(length, input_key): # Definiert eine paarweise Invertierung der Ausgangskonfiguration

    output_key = [0]*length
        
    for k in range(0, M):

        if (input_key[k] == 0): input_key[k] = 1        
        else: input_key[k] = 0
    
        # Hier bitte einmal ausprobieren und das Ergebnis dokumentieren :
        
        if (input_key[0] == 1 or input_key[0] == 0): input_key[0] = 1
        if (input_key[1] == 1 or input_key[1] == 0): input_key[1] = 1
       
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
            L = CNOT(length, GAN_Key)
        
        M = Diskriminator(length, L, reference_key)
        
        for j in range(0, length):

            sum = sum + math.fabs(M[j])

        k = k + 1

        if (sum == float(length)-2):

            return(L)           
            break

def GenerateReferenceKey(keysize):

    for j in range(0, keysize): # Generiere einen zufälligen binären Schlüssel als Referenzwert (entspricht externem und unbekanntem Referenzwert)

        R[j] = random.randint(0,1)
    
    return R
    
def GenerateInitialKey(keysize):

    for j in range(0, keysize): # Generiere einen zufälligen binären Schlüssel als Startwert

        K[j] = random.randint(0,1)

    return K

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.'] # Definiere eine Pythonliste mit Elementen aus dem deutschen Alphabet

with open("EMailString.txt") as file: # Importiere den Zeichenstring aus dem externen File mit Bezeichnung EMailString.txt

    S = file.read()
    
M = 8 # Länge des Schlüssels in Einheiten von Bits

K = ['']*M # Definiere den Schlüssel K als Pythonliste mit der gleichen Anzahl von Elementen wie S     
R = ['']*M # Definiere den Schlüssel R als Pythonliste mit der gleichen Anzahl von Elementen wie S  

fS = ['']*len(S) # Definiere eine Python Liste für den kodierten Zeichenstring als verschlüsselte Zahlenfolge
fSS = '' # Definiere eine Python Liste für den dekodierten Zeichenstring als entschlüsselte Zahlenfolge

dkey = []
ARR_Keys = []

dvalue = 0.0

print('Number of Key Elements : ', len(S))

for k in range(0, len(S)):

    print('Generate Key Element Nr. ', k)

    K = GenerateInitialKey(M) # Generiere den ersten Schlüssel als Startwert für das GAN
    R = GenerateReferenceKey(M) # Generiere einen Referenzschlüssel (anfangs dengelichen Keywert)
        
    K = R # Lege eine Anfangsbedingung mit K = R fest     
    ARR_Keys = ARR_Keys + R # Speichere jeweils den Referenzkey, der modolu CNOT den Key K erzeugt

    key = GAN(M, K, R) # Modelliere ein GAN-Netzwerk zur Rekonstruktion eines möglichen Eingangssignale (bisher unbekannt)

    dvalue = 0.0

    for l in range(0, len(key)):

        dvalue = dvalue + 2**l*key[l]
    
    dkey.append(int(dvalue))

# Binär-zu-Dezimalkonverter einfügen #
# Schleife über unterschiedliche Binärkeys zur Generierung eines dezimalen Schlüssels aus mehreren Komponenten #

for i in range(0,len(S)): # Verschlüsselung der Textzeichen durch den übertragenen Zahlencodes 

    if (S[i] != ' '): fS[i] = (letters_to_value(S[i]) + dkey[i]) % len(alphabet) # Kongruent mod 52
    else: fS[i] = -1

dkey = []

for k in range(0, len(S)):

    print('Generate Key Element Nr. ', k)

    K = GenerateInitialKey(M) # Generiere den ersten Schlüssel als Startwert für das GAN
    R = ARR_Keys[M*k:M*(k+1)] # Nutze jeweils einen Referenzschlüssel

    K = R # Lege eine Anfangsbedigung fest mit K = R
    
    key = GAN(M, K, R) # Modelliere ein GAN-Netzwerk zur Rekonstruktion der Eingangssignale

    dvalue = 0.0

    for l in range(0, len(key)):

        dvalue = dvalue + 2**l*key[l]
    
    dkey.append(int(dvalue))

for j in range(0,len(S)): # Entschlüsselung der Textzeichen durch den übertragenen Zahlencode, welcher aus den Referenzschlüsseln erzeugt wurde.

    if (fS[j] != -1): fSS = fSS + value_to_letters((fS[j] - dkey[j]) % len(alphabet)) # Entschlüsselung im String
    else: fSS = fSS + ' '

print(' ')
print('Verschlüsselte E-Mail : ', fS)
print(' ')
print('Entschlüsselte E-Mail : ',fSS)
print(' ')
