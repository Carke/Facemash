'''
Created on Oct 30, 2011

@author: Carke
'''
# imports and initializers and loading music
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
pygame.mixer.music.set_volume(0.0)
pygame.mixer.music.play(-1)
state = 0
x1=0
y1=0
MusicVolume = 1

#main method
while state == 0:
    MainMenu = pygame.display.set_mode([700,700])
    pygame.display.set_caption("Main Menu")
    event = pygame.event.poll()
    MainMenu.fill([41,89,214])
    MouseOver()
    #draws initial images
    MainMenu.blit(Logo.image, Logo)
    MainMenu.blit(InstructionsButton.image, InstructionsButton)
    MainMenu.blit(PlayButton.image, PlayButton)
    MainMenu.blit(SettingButton.image,SettingButton) 
    MainMenu.blit(AboutButton.image, AboutButton)
    #MainMenu.blit(BackButtonText,(50,520))
    MainMenu.blit(Exit.image, Exit)
    # code for button mouseovers and events
    if Buttons.Collision((SettingButton)):
        if event.type == MOUSEBUTTONUP:
            SettingsWindow()

    if Buttons.Collision((AboutButton)): 
        if event.type == MOUSEBUTTONUP:
            AboutWindow()

    if Buttons.Collision((InstructionsButton)):
        if event.type == MOUSEBUTTONUP:
            InstructionsWindow() 
            
    if Buttons.Collision((PlayButton)):
        if event.type ==  MOUSEBUTTONUP:
            main.play()    
    
    if Buttons.Resize((Exit), (130,70)):
        if event.type == MOUSEBUTTONUP:
            state = 1
            
    pygame.display.update()
    pygame.event.clear()
    # will be exit button currently escape key to end the game.
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 1
        
    
    