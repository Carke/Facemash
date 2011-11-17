'''
Created on Oct 30, 2011

@author: Carke
'''
import pygame, Buttons, main, os
from pygame.locals import *
from Buttons import *
from SettingsWindow import SettingsWindow
from AboutWindow import AboutWindow
from InstructionsWindow import InstructionsWindow
MainMenu = pygame.display.set_mode([700,700])
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("01 - Challenge.ogg")
pygame.display.set_caption("Main Menu")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)
state = 0
x1=0
y1=0
MusicVolume = 1
BackButtonText = pygame.font.Font(None,44).render("Press Escape at any time to exit the game", 1, (0,0,0))

while state == 0:
    MainMenu = pygame.display.set_mode([700,700])
    pygame.display.set_caption("Main Menu")
    event = pygame.event.poll()
    MainMenu.fill([111,159,225])
    MouseOver()
    MainMenu.blit(Logo.image, Logo)
    MainMenu.blit(InstructionsButton.image, InstructionsButton)
    MainMenu.blit(PlayButton.image, PlayButton)
    MainMenu.blit(SettingButton.image,SettingButton) 
    MainMenu.blit(AboutButton.image, AboutButton)
    MainMenu.blit(BackButtonText,(50,520))

    if Buttons.Collision((SettingButton), 280, 70, (55,430, 280,70), "images/settings_hover.png", "images/settings_normal.png", 0):
        if event.type == MOUSEBUTTONDOWN :
            SettingsWindow()

    if Buttons.Collision((AboutButton), 280, 70, (350,430,280,70), "images/about_hover.png","images/about_normal.png", 0): 
        if event.type == MOUSEBUTTONUP:
            AboutWindow()

    if Buttons.Collision((InstructionsButton), 260, 140, (375,225,260,140), "images/learn_hover.png","images/learn_normal.png", 0):
        if event.type == MOUSEBUTTONUP:
            InstructionsWindow() 
            
    if Buttons.Collision((PlayButton), 260, 140, (100,225,260,140),"images/play_hover.png","images/play_normal.png", 0):
        if event.type ==  MOUSEBUTTONUP:
            main.main()    
            
    #print os.path.dirname(os.getcwd())  
    pygame.display.update()
    pygame.event.clear()
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 1
        
    
    