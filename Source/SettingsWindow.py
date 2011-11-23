'''
Created on Oct 31, 2011

@author: Carke
'''
# imports and initializers
import pygame, os, config
from pygame.locals import *
from Buttons import *
from Tkinter import *
from tkFileDialog import askopenfilename
from config import *
pygame.init()
pygame.mixer.init()
MusicVolume = 1
Image = Buttons((160,340,104,56), "images/blank.png", "images/blank.png")
filename = "images/Exit_hover.png"
root=Tk()
root.withdraw()

def SettingsWindow():
    global Image
    pygame.display.quit()
    state = 0
    global MusicVolume
    global RewardImage
    while state == 0:
        SettingsMenu = pygame.display.set_mode([500,570])
        SettingsMenu.fill([41,89,214])
        pygame.display.set_caption("Settings")
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                x1=event.pos[0] 
                y1=event.pos[1]
        #drawing all the initial images and Text
        SettingsMenu.blit(Image.image, Image)
        SettingsMenu.blit(TitleText.image, TitleText)
        BackButtonText = pygame.font.Font("Assets/Fonts/Lobster 1.4.otf",50).render("Select Your Sticker!", 1, (255,255,255))
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
                filename = askopenfilename(filetypes=[("All Files","*"),("jpeg","*.jpg")], initialdir=(os.path.dirname(os.getcwd())))
                Image = ""
                if filename == "":
                    filename = "images/blank.png"
                    config.sticker = "bear"
                else:
                    config.sticker = "custom"
                    config.file = filename
                Image = Buttons((175,340,104,104),filename,filename)
        if Buttons.Collision(Back):
            if event.type == MOUSEBUTTONUP:
                state = 1
        # code for the various default reward stickers
        if Buttons.Resize(Bow, (100,100)):
            if event.type == MOUSEBUTTONUP:
                config.sticker = "bow"
        if Buttons.Resize(Bear, (100,100)):
            if event.type == MOUSEBUTTONUP:
                config.sticker = "bear"
        if Buttons.Resize(Cake, (100,100)):
            if event.type == MOUSEBUTTONUP:
                config.sticker = "cake"
        Buttons.Resize(Image, (104,104))
        pygame.event.clear()
        pygame.display.update()