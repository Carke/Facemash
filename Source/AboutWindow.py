'''
Created on Nov 1, 2011

@author: Carke
'''
import pygame
from pygame.locals import *
from Buttons import *
def AboutWindow():
    pygame.event.clear()
    pygame.display.quit()
    setting = 0
    while setting == 0:
        AboutMenu = pygame.display.set_mode([500,570])
        pygame.display.set_caption("About")
        AboutMenu.fill([41,89,214])
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                x1=event.pos[0] 
                y1=event.pos[1]
        AboutMenu.blit(AboutTitleText.image, AboutTitleText)
        AboutMenu.blit(Back.image, Back)
        AboutMenu.blit(AboutText.image, AboutText)
        if Buttons.Collision(Back):
            if event.type == MOUSEBUTTONUP:
                pygame.event.clear()
                setting = 1
                
        pygame.display.update()