##################################################################################################################################################################
#                                                                                                                                                                #
#   Autoren: Sven Engels und Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                                                #
##################################################################################################################################################################

# PYTHON ROUTINE zur Verschlüsselung von E-Mails durch ein GAN-basiertes künstliches neuronales Netzwerk #

# @ Sven Engels: Die Strukturerkennung funktioniert genauso wie der Test auf valide Schlüssel. Als Struktur kann man hier weiterführend auch Python-Strings anstatt binärer Zahlenwerte verwenden bzw. mehrzeilige Binärcodes auf Vailidität testen. 

# Allgemein: Es wurde in dieser aktuellesten Version eine Invertierende Schaltung verwendet - siehe Funktions-Definition unter CNOT.

#Programm zu validierung von Passwörtern mit einer Länge von 8 Zeichen mithilfe von GAN-Algorithmus
#Eingabe über Datei oder Konsole
#überprüfung wahlweise auf:
# -min. drei Sonderzeichen
# -min. drei Sonderzeichen und min. eine Zahl
# -min. drei Sonderzeichen, min. eine Zahl und min. einen Großbuchstaben

import os
import sys
import statistics
import math
import random

#Komplexity:
# 1-> nur Sonderzeichen
# 2-> Sonderzeichen und Zahlen
# 3-> Sonderzeichen, Zahlen und Großbuchstaben
komplexity = 3

#input_option:
# 1-> aus Datei
# 2-> über Konsole
input_option = 1

# Definition von Funktionen zur Verschlüsselung a kongruent b mod 52 durch GAN
def letters_to_value(x): # Definiere eine Funktion zur Abbildung von Buchstaben auf Zahlen a kongruent b mod 52 (bzw. eine höhere Anzahl von Buchstaben)
    
    x_value = 0

    if (x == 'a') : x_value = 0
    if (x == 'b') : x_value = 0
    if (x == 'c') : x_value = 0
    if (x == 'd') : x_value = 0
    if (x == 'e') : x_value = 0
    if (x == 'f') : x_value = 0
    if (x == 'g') : x_value = 0
    if (x == 'h') : x_value = 0
    if (x == 'i') : x_value = 0
    if (x == 'j') : x_value = 0
    if (x == 'k') : x_value = 0
    if (x == 'l') : x_value = 0
    if (x == 'm') : x_value = 0
    if (x == 'n') : x_value = 0
    if (x == 'o') : x_value = 0
    if (x == 'p') : x_value = 0
    if (x == 'q') : x_value = 0
    if (x == 'r') : x_value = 0
    if (x == 's') : x_value = 0
    if (x == 't') : x_value = 0
    if (x == 'u') : x_value = 0
    if (x == 'v') : x_value = 0
    if (x == 'w') : x_value = 0
    if (x == 'x') : x_value = 0
    if (x == 'y') : x_value = 0
    if (x == 'z') : x_value = 0
    if (x == 'ä') : x_value = 0
    if (x == 'ö') : x_value = 0
    if (x == 'ü') : x_value = 0
    if (x == 'ß') : x_value = 0
    

    if (komplexity == 3): val2=3
    elif (komplexity <= 2): val2=0

    if (x == 'A') : x_value = val2
    if (x == 'B') : x_value = val2
    if (x == 'C') : x_value = val2
    if (x == 'D') : x_value = val2
    if (x == 'E') : x_value = val2
    if (x == 'F') : x_value = val2
    if (x == 'G') : x_value = val2
    if (x == 'H') : x_value = val2
    if (x == 'I') : x_value = val2
    if (x == 'J') : x_value = val2
    if (x == 'K') : x_value = val2
    if (x == 'L') : x_value = val2
    if (x == 'M') : x_value = val2
    if (x == 'N') : x_value = val2
    if (x == 'O') : x_value = val2
    if (x == 'P') : x_value = val2
    if (x == 'Q') : x_value = val2
    if (x == 'R') : x_value = val2
    if (x == 'S') : x_value = val2
    if (x == 'T') : x_value = val2
    if (x == 'U') : x_value = val2
    if (x == 'V') : x_value = val2
    if (x == 'W') : x_value = val2
    if (x == 'X') : x_value = val2
    if (x == 'Y') : x_value = val2
    if (x == 'Z') : x_value = val2
    if (x == 'Ä') : x_value = val2
    if (x == 'Ö') : x_value = val2
    if (x == 'Ü') : x_value = val2
    

    if(komplexity >= 2): val3=2
    elif(komplexity == 1): val3=0
    
    if (x == '0') : x_value = val3
    if (x == '1') : x_value = val3
    if (x == '2') : x_value = val3
    if (x == '3') : x_value = val3
    if (x == '4') : x_value = val3
    if (x == '5') : x_value = val3
    if (x == '6') : x_value = val3
    if (x == '7') : x_value = val3
    if (x == '8') : x_value = val3
    if (x == '9') : x_value = val3

    #verschidene Sonderzeichen machen Probleme(' ` ´ \ ) bezogen auf deutsche tastatur und nur auf Tasten gekenzeichnete Sonderzeichen
    val4=1
    if (x == '.') : x_value = val4
    if (x == ',') : x_value = val4
    if (x == '-') : x_value = val4
    if (x == '_') : x_value = val4
    if (x == ';') : x_value = val4
    if (x == ':') : x_value = val4
    if (x == '#') : x_value = val4
    if (x == '+') : x_value = val4
    if (x == '*') : x_value = val4
    if (x == '~') : x_value = val4
    if (x == '!') : x_value = val4
    if (x == '"') : x_value = val4
    #if (x == '§') : x_value = val4
    if (x == '$') : x_value = val4
    if (x == '%') : x_value = val4
    if (x == '&') : x_value = val4
    if (x == '/') : x_value = val4
    if (x == '\\') : x_value = val4 # hier kommt es auf das \\ an wenn nur einfach fehler 
    if (x == '{') : x_value = val4
    if (x == '(') : x_value = val4
    if (x == '[') : x_value = val4
    if (x == ')') : x_value = val4
    if (x == ']') : x_value = val4
    if (x == '=') : x_value = val4
    if (x == '}') : x_value = val4
    if (x == '?') : x_value = val4
    #if (x == '°') : x_value = val4
    if (x == '^') : x_value = val4
    #if (x == 'µ') : x_value = val4
    if (x == '<') : x_value = val4
    if (x == '>') : x_value = val4
    if (x == '|') : x_value = val4
    if (x == '@') : x_value = val4
    #if (x == '€') : x_value = val4
    if (x == ' ') : x_value = val4

    return x_value

# Definition von Funktionen zur Verschlüsselung b kongruent a mod 52 durch GAN

# Generiert einen zufälligen binären Schlüssel mit übergebener Länge
def Generator(length, input_key, train):

#input_key und train werden nicht verwendet?
    output_key = [0]*length

    for j in range(0, length): # Generiere einen zufälligen binären Schlüssel zum Abgleich mit dem Referenzschlüssel

        output_key[j] = random.randint(0,komplexity)

    return(output_key)

#berrechnet die Differenz zweier binär-Listen elementweise     
def Diskriminator(length, input_key, ideal_key):

    difference1 = [0]*length

    for j in range(0, length):
        #math.fabs gibt absoluten Wert als float zurück(keine negativen Werte) 
        difference1[j] = math.fabs(ideal_key[j] - input_key[j]) # Berechne die Abweichung zwischen Referenzschlüssel und dynamisch generiertem Schlüssel

    return(difference1)

#Gibt die Passwort Bedingungen vor
def CNOT(length, input_key): # Definiert eine paarweise Invertierung der Ausgangskonfiguration

    output_key = [0]*length

    # M(global) anstelle von length benutzt    
    #for k in range(0, M):

#variabeln müssen vor der For Schleife definiert werden sonst keine Funktion!    
    j  = random.randint(0, length-1)
    l  = random.randint(0, length-1)
    m  = random.randint(0, length-1)
    #if(komplexity >= 2): f  = random.randint(0, length-1)
    #if(komplexity == 3): z  = random.randint(0, length-1)

    #j, l, m dürfen nicht gleich sein
    while l == j:
        l  = random.randint(0, length-1)

    while m == j or m == l:
        m  = random.randint(0, length-1)
    
    if(komplexity >= 2):     
        f  = random.randint(0, length-1)
        while f == j or f == l or f == m:
            f  = random.randint(0, length-1)
    if(komplexity == 3):
        z  = random.randint(0, length-1)
        while z == j or z == l or z == m or z == f:
            z  = random.randint(0, length-1)    
        
    for k in range(0, length):

        if (input_key[k] == 0): input_key[k] = 1        
        elif(input_key[k] == 2 and komplexity == 2): input_key[k] = 2
        elif(input_key[k] == 2 and komplexity == 3): input_key[k] = 3
        elif(input_key[k] == 3 and komplexity == 3): input_key[k] = 2
        else: input_key[k] = 0

        # @ Sven Engels: Hier werden die Bedingungen an die Validität von (binären) Referenzwerten festgelegt und dann der Schlüssel aus KetStructure.txt mit dynamischen Schlüsselwerten aus dem GAN verglichen. Zum Beispiel: Valide Referenzschlüssel sollen an bestimmten Stellen der Zahlenkombination eine 1 festgelegt haben.

        # Hier bitte einmal durch Festlegen unterschiedlicher Kriterien ausprobieren und das Ergebnis dokumentieren :

        input_key[j] = 1
        input_key[l] = 1
        input_key[m] = 1

        if(komplexity >= 2): input_key[f] = 2
        if(komplexity == 3): input_key[z] = 3

        output_key[k] = input_key[k]
    
    #print(l,m,f,z)
    return output_key

def GAN(length, initial_key, reference_key, iterations):

    k = 0
    GAN_Key = [0]*length # Definiere den GAN-Schlüssel mit der Variable GAN_Key als Pythonliste mit der gleichen Anzahl von Elementen wie die anderen Keys 
    Me = [0]*length #M war schon global für die Schlüssellänge in verwendung

    while(True):
        
        sum = 0.0
        initial_key = CNOT(length, initial_key)
        
#initial key und referenz key werden hier nicht verwendet ?
        if (k == 0): 
            L = Generator(length, initial_key, reference_key)

        if (k > 0): 

            GAN_Key = Generator(length, L, Me)
            initial_key = GAN_Key
            L = CNOT(length, GAN_Key)
        
        Me = Diskriminator(length, L, reference_key)

        for j in range(0, length):

            sum = sum + math.fabs(Me[j])

        k = k + 1

#funktion der zahl??
        #wenn sum == 8.0-3  (5)
        # 3 bei 0-1
        # 3 bei 0-2
        # 1 bei 0-3
        if(komplexity == 3):
            if (sum == float(length)-1):

                return(initial_key)
                break
        else:
            if (sum == float(length)-3):

                return(initial_key)
                break

#Problem der ab und zu auftretenden Endlosschleife beheben(erst bei 0-3)    
        if(k> iterations): 
            return(initial_key)
            break

#überprüft anhand der Quersumme der durch die Funktion letters_to_value erzeugten Dezimalen Liste ob Passwort einen ausreichend großen Wert hat
def checkforvalidity(input_string, komplexity_val):
    
    dezstring = ['']*len(input_string)
    sum = 0

    #konvertiere Zeichen String in Dezimale Liste 
    for k in range(0, len(input_string)):
        dezstring[k] = int(letters_to_value(input_string[k]))
        sum = sum + dezstring[k]

    if(komplexity_val == 1):
        #1+1+1
        if(sum >= 3): return True
        else: return False
    elif(komplexity_val == 2):
        #1+1+1+2
        if(sum >= 5): return True
        else: return False
    elif(komplexity_val == 3):
        #1+1+1+2+3
        if(sum >= 8): return True
        else: return False

#generiert einen zufälligen Schlüssel
def GenerateReferenceKey(keysize):

    for j in range(0, keysize): # Generiere einen zufälligen binären Schlüssel als Referenzwert (entspricht externem und unbekanntem Referenzwert)

        R[j] = random.randint(0,komplexity)
    
    return R

#generiert einen zufälligen Schlüssel    
def GenerateInitialKey(keysize):

    for j in range(0, keysize): # Generiere einen zufälligen binären Schlüssel als Startwert

        K[j] = random.randint(0,komplexity)

    return K

#
# @ Sven Engels : Hier kann man die Routine dahingehen verwenden, um binäre Werte zu vergleichen. Z. B. zur Falschgeld- bzw. Binärstrukturerkennung erkennung.
#

#Input von Datei
if(input_option == 1):
    with open("projekt\KeyStructure.txt") as file: # Importiere den Zeichenstring aus dem externen File mit Bezeichnung KeyDeclaration.txt

        S = file.read()
    print('Zu prüfendes Passwort: ', S)

#Konsoleneingabe
if(input_option == 2):
    S = input("Bitte das zu prüfende Passwort eingeben (Länge 8 Zeichen):")
    if('§' in S):
        print('Nicht unterstütztes Zeichen gefunden! (§)')
        sys.exit()
    elif('€' in S):
        print('Nicht unterstütztes Zeichen gefunden! (€)')
        sys.exit()
    elif('°' in S):
        print('Nicht unterstütztes Zeichen gefunden! (°)')
        sys.exit()
    elif('µ' in S):
        print('Nicht unterstütztes Zeichen gefunden! (µ)')
        sys.exit()
    elif(len(S) < 8): 
        print("Falsche Länge erkannt! (zu kurz)")
        sys.exit()
    elif(len(S) > 8): 
        print("Falsche Länge erkannt! (zu lang)")
        sys.exit()
    elif (len(S) == 8):
            print("Start der Validierung...")
    #print(S)
#    sys.exit()

M = len(S) # Länge des Schlüssels in Einheiten von Bits

K = ['']*M # Definiere den Schlüssel K als Pythonliste mit der gleichen Anzahl von Elementen wie S     
R = ['']*M # Definiere den Schlüssel R als Pythonliste mit der gleichen Anzahl von Elementen wie S  

print('Number of Key Elements: ', len(S))

trials = 100000
difference = 0.0

for k in range(0, trials):

    if(checkforvalidity(S,komplexity) == False): 
        print(' ')
        print('Quersummen Kriterium nicht erfüllt. Passwort kann nicht valide sein!')
        print(' ')
        sys.exit()

    print('Comparing Generated Key Element Nr. ', k)
    difference = 0.0

    K = GenerateInitialKey(M) # Generiere den ersten Schlüssel als Startwert für das GAN
    R = GenerateReferenceKey(M) # Generiere einen Referenz Schlüssel
    
    key = GAN(M, K, R, trials) # Modelliere ein GAN-Netzwerk zur Rekonstruktion eines der möglichen Eingangssignale (bisher unbekannt)
    
    for j in range(0, len(S)): # Berechne mit dem GAN (Schaltung) kompatible Werte 

        difference = difference + math.fabs(float(key[j]) - float(letters_to_value(S[j])))

    if (difference == 0.0): # Für übereinstimmende Schlüsselwerte (Dezimalcodes mit difference = 0.0) wird die Validität bestätigt

        print(' ')
        print('Passwort ist valide.')
        print(' ')
        print('geprüftes Passwort: ', S)
        print(' ')
        print('Referenzcode: ', key)

        break

    if (k == trials-1):
        
        print(' ')
        print('Passwort erfüllt die erforderlichen Kriterien nicht!')
        print(' ')
       
#########################################################
#                                                       #
# TO DOs:                                               #
#                                                       #
# 1: Source Code anpassen für Umlaute       x           #
# 2: Schaltung ggfalls anpassen             x           #
# 3: Weitere Features integrieren           x           #
#                                                       #
#########################################################
 
