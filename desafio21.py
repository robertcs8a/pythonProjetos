import pygame
from pygame import mixer

pygame.init()
pygame.mixer.music.load('A Dois Passos Do Paraíso - Blitz.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
