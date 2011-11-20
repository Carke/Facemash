'''
Created on Oct 31, 2011

@author: Carke
'''
# imports and initializers
import pygame, os
from pygame.locals import *
from Buttons import *
from Tkinter import *
from tkFileDialog import askopenfilename
root = Tk()
pygame.init()
pygame.mixer.init()
MusicVolume = 1
color = (255,255,255)
Image1 = Buttons((160,350,104,56), "images/blank.png", "images/blank.png")
root=Tk()
    

def SettingsWindow():
    global Image1
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
        #drawing all the initial images and Text
        SettingsMenu.blit(Image1.image, Image1)
        SettingsMenu.blit(TitleText.image, TitleText)
        BackButtonText = pygame.font.Font("LOBSTER 1.4.OTF",50).render("Select Your Sticker!", 1, (255,255,255))
        SettingsMenu.blit(BackButtonText,(60,200))
        SettingsMenu.blit(AudioText.image, AudioText)
        SettingsMenu.blit(AudioON.image, AudioON)
        SettingsMenu.blit(AudioOFF.image, AudioOFF)
        SettingsMenu.blit(Upload.image, Upload)
        SettingsMenu.blit(Back.image, Back)
        SettingsMenu.blit(Bow.image, Bow)
        SettingsMenu.blit(Bear.image, Bear)
        SettingsMenu.blit(Cake.image, Cake)
        # code for turning the Audio On and displaying that it is on
        if Buttons.Resize(AudioON, (104,56)):
            if event.type ==  MOUSEBUTTONUP:
                pygame.mixer.music.set_volume(1.0)
                MusicVolume = 1
        if MusicVolume == 1: 
            SettingsMenu.blit(AudioON.hover, AudioON)
        #code for turning the audio off and displaying that it is off
        if Buttons.Resize(AudioOFF, (104,56)):
            if event.type ==  MOUSEBUTTONUP:
                pygame.mixer.music.set_volume(0.0)
                MusicVolume = 0
        if MusicVolume == 0: 
            SettingsMenu.blit(AudioOFF.hover, AudioOFF)
        # code for uploading your own image
        if Buttons.Resize(Upload, (130,70)):
            if event.type == MOUSEBUTTONUP :
                # uses Tkinter to determine what file types are accepted and where to look initially, can go to any directory
                filename = askopenfilename(filetypes=[("All Files","*"),("jpeg","*.jpg")], initialdir=(os.path.dirname("C:\Users")))
                Image1 = Buttons((175,350,104,104),filename,filename)
                v = Image1
        if Buttons.Collision(Back, 195, 68, (300,450,195,68), "images/Back_hover.png", "images/Back_normal.png"):
            if event.type == MOUSEBUTTONUP:
                state = 1
        # code for the various default reward stickers
        if Buttons.Resize(Bow, (100,100)):
            if event.type == MOUSEBUTTONUP:
                RewardImage = Bow
        if Buttons.Resize(Bear, (100,100)):
            if event.type == MOUSEBUTTONUP:
                RewardImage = Bear
        if Buttons.Resize(Cake, (100,100)):
            if event.type == MOUSEBUTTONUP:
                RewardImage = Cake
        Buttons.Resize(Image1, (104,104))
        pygame.event.clear()
        pygame.display.update()