import pygame
import time

# Initialisierung von pygame
pygame.mixer.init()

# Einige Klänge laden (Beispielklänge)
kick = pygame.mixer.Sound('kick.wav')
snare = pygame.mixer.Sound('snare.wav')

# Funktion für einen einfachen Beat
def play_beat():
    kick.play()
    time.sleep(0.5)  # Halbe Sekunde warten
    snare.play()
    time.sleep(0.5)  # Halbe Sekunde warten

# Den Beat abspielen
for i in range(4):  # Wiederhole den Beat 4 Mal
    play_beat()
