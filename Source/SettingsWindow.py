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
color = (255,255,255)

def SettingsWindow():
    pygame.display.quit()
    state = 0
    global MusicVolume
    global v
    while state == 0:
        SettingsMenu = pygame.display.set_mode([500,500])
        SettingsMenu.fill([111,159,225])
        pygame.display.set_caption("Settings")
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                x1=event.pos[0] 
                y1=event.pos[1]
        SettingsMenu.blit(TitleText.image, TitleText)
        BackButtonText = pygame.font.Font("LOBSTER 1.4.OTF",50).render("Select Your Sticker!", 1, (255,255,255))
        SettingsMenu.blit(BackButtonText,(60,200))
        SettingsMenu.blit(AudioText.image, AudioText)
        SettingsMenu.blit(AudioON.image, AudioON)
        SettingsMenu.blit(AudioOFF.image, AudioOFF)
        #SettingsMenu.blit(Image1.image, Image1)
        if Buttons.Resize(AudioON, (104,56)):
            if event.type ==  MOUSEBUTTONUP:
                pygame.mixer.music.set_volume(1.0)
                MusicVolume = 1
        if MusicVolume == 1: 
            SettingsMenu.blit(AudioON.hover, AudioON)
        if Buttons.Resize(AudioOFF, (104,56)):
            if event.type ==  MOUSEBUTTONUP:
                pygame.mixer.music.set_volume(0.0)
                MusicVolume = 0
        if MusicVolume == 0: 
            SettingsMenu.blit(AudioOFF.hover, AudioOFF)
#        if Buttons2.Collision(Image1):
#            if event.type == MOUSEBUTTONUP:
#                image = Image1
#        if Buttons2.Collision(Image2):
#            if event.type == MOUSEBUTTONUP:
#                image = Image2
#        if Buttons2.Collision(Image3):
#            if event.type == MOUSEBUTTONUP:
#                image = Image3
#        if Buttons.Collision(BackButton):
#            Quit()
        pygame.event.clear()
            
            
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                state = 1