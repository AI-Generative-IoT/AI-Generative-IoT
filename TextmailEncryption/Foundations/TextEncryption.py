################################################################################################################################################
#                                                                                                                                              #
#   Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                              #
################################################################################################################################################

# BASIS PYTHON ROUTINE zur Verschlüssleung von Textnachrichten #

import os
import sys
import math

import random

def compare_letters(x): # Definiere eine Funktion zur Abbildung von Buchstaben auf Zahlen a kongruent b mod 26
    
    x_value = 0

    if (x == 'a' or x == 'A') : x_value = 0
    if (x == 'b' or x == 'B') : x_value = 1
    if (x == 'c' or x == 'C') : x_value = 2
    if (x == 'd' or x == 'D') : x_value = 3
    if (x == 'e' or x == 'E') : x_value = 4
    if (x == 'f' or x == 'F') : x_value = 5
    if (x == 'g' or x == 'G') : x_value = 6
    if (x == 'h' or x == 'H') : x_value = 7
    if (x == 'i' or x == 'I') : x_value = 8
    if (x == 'j' or x == 'J') : x_value = 9
    if (x == 'k' or x == 'K') : x_value = 10
    if (x == 'l' or x == 'L') : x_value = 11
    if (x == 'm' or x == 'M') : x_value = 12
    if (x == 'n' or x == 'N') : x_value = 13
    if (x == 'o' or x == 'O') : x_value = 14
    if (x == 'p' or x == 'P') : x_value = 15
    if (x == 'q' or x == 'Q') : x_value = 16
    if (x == 'r' or x == 'R') : x_value = 17
    if (x == 's' or x == 'S') : x_value = 18
    if (x == 't' or x == 'T') : x_value = 19
    if (x == 'u' or x == 'U') : x_value = 20
    if (x == 'v' or x == 'V') : x_value = 21
    if (x == 'w' or x == 'W') : x_value = 22
    if (x == 'x' or x == 'X') : x_value = 23
    if (x == 'y' or x == 'Y') : x_value = 24
    if (x == 'z' or x == 'Z') : x_value = 25

    return x_value

def compare_numbers(x): # Definiere eine Funktion zur Abbildung von Zahlen auf Buchstaben a kongruent b mod 26
     
    x_value = ''

    if (x == 0) : x_value = 'a' or x == 'A'
    if (x == 1) : x_value = 'b' or x == 'B'
    if (x == 2) : x_value = 'c' or x == 'C'
    if (x == 3) : x_value = 'd' or x == 'D'
    if (x == 4) : x_value = 'e' or x == 'E'
    if (x == 5) : x_value = 'f' or x == 'F'
    if (x == 6) : x_value = 'g' or x == 'G'
    if (x == 7) : x_value = 'h' or x == 'H'
    if (x == 8) : x_value = 'i' or x == 'I'
    if (x == 9) : x_value = 'j' or x == 'J'
    if (x == 10) : x_value = 'k' or x == 'K'
    if (x == 11) : x_value = 'l' or x == 'L'
    if (x == 12) : x_value = 'm' or x == 'M'
    if (x == 13) : x_value = 'n' or x == 'N'
    if (x == 14) : x_value = 'o' or x == 'O'
    if (x == 15) : x_value = 'p' or x == 'P'
    if (x == 16) : x_value = 'q' or x == 'Q'
    if (x == 17) : x_value = 'r' or x == 'R'
    if (x == 18) : x_value = 's' or x == 'S'
    if (x == 19) : x_value = 't' or x == 'T'
    if (x == 20) : x_value = 'u' or x == 'U'
    if (x == 21) : x_value = 'v' or x == 'V'
    if (x == 22) : x_value = 'w' or x == 'W'
    if (x == 23) : x_value = 'x' or x == 'X'
    if (x == 24) : x_value = 'y' or x == 'Y'
    if (x == 25) : x_value = 'z' or x == 'Z'

    return x_value

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Definiere eine Pythonliste mit Elementen aus dem deutschen Alphabet
S = 'Eine alte Dame geht heute einkaufen' # Definiere einen Zeichenstring zur Kodierung und Dekodierung

N = 1000 # Gesamte Anzahl der Iterationen

K = ['']*len(S) # Definiere den Schlüssel als Pythonliste mit der gleichen Anzahl von Elementen wie S     
fS = ['']*len(S) # Definiere den kodierten Zeichenstring als verschlüsselte Zahlenfolge
fSS = '' # Definiere den dekodierten Zeichenstring als entschlüsselte Zahlenfolge

histogramm = [0]*len(alphabet) # Definiere das Histogramm mit Häufigkeitsverteilung der Buchstaben

for j in range(0,len(S)): # Generiere einen zufällgien Schlüssel

    K[j] = random.randint(0,N)

for i in range(0,len(S)): # Verschlüsselung der Zahlencodes zu den Buchstaben im String S

    if (S[i] != ' '): fS[i] = (compare_letters(S[i]) + K[i]) % len(alphabet) # Kongruent mod 26
    else: fS[i] = -1

word_count = 0
sum = 0 

for j in range(0,len(alphabet)): # Zähle die Anzahl der Wörter im verschlüssleten String f(S) = fS

    word_count = fS.count(compare_letters(alphabet[j])) # Zähle die Buchstaben
    histogramm[j] = float(word_count) # Definiere das Histogramm

for j in range(0, len(histogramm)): # Gebe das Histogramm auf dem Bildschirm aus

    print(alphabet[j], histogramm[j]) # Ausgabe der Werte
    sum = sum + histogramm[j] # Gesamtsumme

print('Anzahl der Buchstaben: ', sum) # Bildschirmausgabe
print('Zeichenfolge im verschlüsselten String: ', fS) # Gebe die Zeichenfolge im verschlüsselten String aus

for j in range(0,len(S)): # Entschlüsselung der Zahlencodes zu den Buchstaben im String S

    if (fS[j] != -1): fSS = fSS + compare_numbers((fS[j] - K[j]) % len(alphabet)) # Entschlüsselung im String
    else: fSS = fSS + ' '

print('Dekodierter Zeichenstring:', fSS) # Gebe den dekodierten Zeichenstrign zurück
