'''
Created on Nov 2, 2011

@author: Carke
'''
import pygame
from pygame.locals import *
from Buttons import *
        
def InstructionsWindow():
    global InstructionsTitleText
    pygame.display.quit()
    setting = 0
    while setting == 0:
        InstructionsMenu = pygame.display.set_mode([500,500])
        pygame.display.set_caption("Instructions")
        InstructionsMenu.fill([111,159,225])
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                x1=event.pos[0] 
                y1=event.pos[1]
        InstructionsMenu.blit(InstructionsTitleText.image, InstructionsTitleText)
        Buttons.Resize(InstructionsTitleText, (511,141))
        InstructionsMenu.blit(Back.image, Back)
        if Buttons.Collision(Back, 195, 68, (300,450,195,68), "images/Back_hover.png", "images/Back_normal.png", 0):
            if event.type == MOUSEBUTTONDOWN:
                setting = 1
        pygame.display.update()
