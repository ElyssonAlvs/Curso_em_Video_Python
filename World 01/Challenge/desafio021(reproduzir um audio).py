"""import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3') -> o comando n é legível com a versão do pycharm e do python dando por fim um error de execução
pygame.mixer.music.play()
pygame.event.wait()"""
import playsound  # Biblioteca usada para reproduzir o áudio
playsound.playsound('ex021.mp3')  # Toca o áudio autimaticamente