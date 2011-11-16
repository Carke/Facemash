'''
Created on Oct 31, 2011

@author: Carke
'''
import pygame, os
from pygame.locals import *
from Buttons import *
pygame.init()
pygame.mixer.init()
MusicVolume = 1

def SettingsWindow():
    pygame.display.quit()
    state = 0
    global MusicVolume
    while state == 0:
        SettingsMenu = pygame.display.set_mode([500,500])
        SettingsMenu.fill([111,159,225])
        pygame.display.set_caption("Settings")
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                x1=event.pos[0] 
                y1=event.pos[1]
        SettingsMenu.blit(TitleText.image, TitleText)
        BackButtonText = pygame.font.Font(None,32).render("Press Escape to go back.", 1, (0,0,0))
        SettingsMenu.blit(BackButtonText,(100,450))
        SettingsMenu.blit(AudioText.image, AudioText)
        SettingsMenu.blit(AudioON.image, AudioON)
        SettingsMenu.blit(AudioOFF.image, AudioOFF)
        #SettingsMenu.blit(Image1.image, Image1)
        if AudioON.Rect.collidepoint((x1,y1)):
            SettingsMenu.blit(AudioON.hover, AudioON)
            if event.type ==  MOUSEBUTTONUP:
                pygame.mixer.music.set_volume(1.0)
                MusicVolume = 1
        if MusicVolume == 1: 
            SettingsMenu.blit(AudioON.hover, AudioON)
        if AudioOFF.Rect.collidepoint((x1,y1)):
            SettingsMenu.blit(AudioOFF.hover, AudioOFF)
            if event.type ==  MOUSEBUTTONUP:
                pygame.mixer.music.set_volume(0.0)
                MusicVolume = 0
        if MusicVolume == 0: 
            SettingsMenu.blit(AudioOFF.hover, AudioOFF)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                state = 1
        pygame.event.clear()
            
            
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                state = 1