import pygame
from pygame.locals import *
from MainMenu import *

def check():
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		return 0
	if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
		return 0