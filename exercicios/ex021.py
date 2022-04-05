#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
nome = str(input('Qual é seu nome?'))
print(f'{nome}, você irá para o Beto Carreiro!')
# Inicializando o mixer PyGame
pygame.mixer.init()
# Iniciando o Pygame
pygame.init()
pygame.mixer.music.load('ex021b.mp3')
pygame.mixer.music.play()
pygame.event.wait()

