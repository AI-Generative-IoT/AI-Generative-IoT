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
    difference = [0.0] * (length)
    for j in range(0, length):
        difference[j] = math.fabs(ideal_key[j] - input_key[j])
    return (difference)

def CNOT1(length, input_key):
    output_key = input_key
    for m in range(0, length):
        if input_key[m] == 1:
            output_key[m - 1] = (input_key[m-1] + 1) % 2
    return output_key

def CNOT2(length, input_key):
    cn = random.randint(0, 10)
    cc = random.randint(3, 7)
    if (cn < cc):
        cn = 0
    else:
        cn = 1
    output_key = input_key
    for m in range(0, length):
        if input_key[m] == cn:
            output_key[m - 1] = (input_key[m - 1] + 1) % 2
    return output_key

def GAN(length, initial_key, reference_key):
    i = 0
    GAN_Key = [1] * length  # Definiere den GAN-Schlüssel GAN_Key als Pythonliste mit der gleichen Anzahl von Elementen wie die anderen Keys

    while (True):
        sum = 0.0
        if meth != 2:
            initial_key = CNOT1(length, initial_key)
        else:
            initial_key = CNOT2(length, initial_key)
        if (i == 0):
            L = Generator(length, initial_key, GAN_Key)
        else:
            if meth != 2:
                L = CNOT1(length, Generator(length, L, M))
            else:
                L = CNOT2(length, Generator(length, L, M))

        M = Diskriminator(length, L, reference_key)
        for j in range(0, length):
            sum = sum + M[j]
        i += 1
        if meth == 3:
            if (sum < 2.0):
                return (GAN_Key)
            else:
                GAN_Key = L
        else:
            if (sum == 0.0):
                return (GAN_Key)
            else:
                GAN_Key = L


def GenerateInitialKey(keysize):
    for j in range(0, keysize):  # Generiere einen zufälligen binären Schlüssel als Referenzwert (entspricht externem und unbekanntem Referenzwert)
        KI[j] = random.randint(0, 1)
    return KI

def GenerateReferenceKey(keysize):
    for j in range(0, keysize):  # Generiere einen zufälligen binären Schlüssel als Referenzwert (entspricht externem und unbekanntem Referenzwert)
        KR[j] = random.randint(0, 1)
    return KR

def umwandeln(i): # umwandeln Zeichenkette aus Zahlen in Intergerzahlen
    z = ''
    while S[i]!= ' ': # Leerzeichen ist Trennzeichen in Datei
        z += S[i]
        i += 1
    return(z, i)

def ents():
    fSS = ''  # entschlüsselter Text
    for i in range(0, len(fS)): # Verschlüsselung von E-Mails durch den übertragenen Zahlencode
        erg = (fS[i] - dkey[i]) % la
        if erg == 172:
            fSS = fSS + chr(8364)
        elif erg == 48:
            fSS = fSS + chr(8240)
        else:
            for j in range(0, la):
                if j == erg:
                    fSS = fSS + chr(j)  # Entschlüsselung im String
                    break
    return(fSS)

##########################################################################################################################


print('\nFür die Entschlüsselung sind folgende Methoden möglich:')
print('1: Der verschlüsselte Text wird unverändert übernommen')
print('2: Es gibt zwei Versionen der Funktion CNOT')
print('3: Die Funktion GAN wird beendet, wenn sum < 2 ist')
print('0: Abbruch des Programmes \n')

tf = True
while tf:
    meth = input('Welche Methode soll angewendet werden? ')  # Auswahl der Variante
    print('\n')
    if meth == '0':
        exit()
    elif meth not in ['1', '2', '3']:
        print('falsche Eingabe')
    else:
        meth = int(meth)
        tf = False

with open("Schlüssel.txt") as file:
    S = file.read()  # enthält verschlüsselte Zeichenanzahl, verschlüsselte Zeichen und dkey aus Programm "verschlüsseln"

i = 0
ze = umwandeln(i)
i = ze[1] + 1
u = int(ze[0])
v = ze[0]
l = int((int(ze[0]) - 27)/2)

fS =[]  #fS und dkey für Entschlüsselung (S trennen)

for z in range(0, l):
    ze = umwandeln(i)
    fS.append(int(ze[0]))
    i = ze[1] + 1
i += 1

dkey = []
for z in range(0, l):
    ze = umwandeln (i)
    dkey.append(int(ze[0]))
    i = ze[1] + 1

la = 256


fSS = ents()
print('Entschlüsselte E-Mail:\r\n' + fSS)
print('Generated Decimal Key: ', dkey)

# Erstellung Irreversibilität des Textes
M = 8       # Definiere Schlüssellänge
KI = ['']*M  # Definiere den Schlüssel KI als Pythonliste
KR = ['']*M  # Definiere den Schlüssel KR als Pythonliste
I = ['']*M  # Definiere den Schlüssel I als Pythonliste mit der gleichen Anzahl von Elementen wie S
R = ['']*M  # Definiere den Schlüssel R als Pythonliste mit der gleichen Anzahl von Elementen wie S
dkey = []

for k in range(0, l):
    I = GenerateInitialKey(M)  # Generiere den ersten Schlüssel als Startwert für das GAN
    R = GenerateReferenceKey(M)
    key = GAN(M, I, R)  # Modelliere ein GAN-Netzwerk zur Rekonstruktion möglicher Eingangssignale (bisher unbekannt)
    dvalue = 0

    for j in range(0, M):
       dvalue = dvalue + 2 ** j * key[j]
    dkey.append(dvalue)

if meth != 1:
    fSS = ents()



with open("Schlüssel.txt", 'w') as datei:
    datei.write(v + ' ')
    if meth == 1:
        for i in range(0, len(fS)):
            datei.write(str(fS[i]) + ' ')
 #           datei.write(str(random.randint(0, 255)) + ' ') # Version ohne GAN
        datei.write('\n')
    else:
        for i in range(0, len(fSS)):
            if (ord(fSS[i]) > 31 and ord(fSS[i]) < 128) or ord(fSS[i]) > 160:
                datei.write(str(random.randint(0, 255)) + ' ')
            else:
                datei.write(str(ord('*')) + ' ')
        datei.write('\n')

    for i in range(0, len(dkey)):
        datei.write(str(dkey[i]) + ' ')
    datei.write('\n')