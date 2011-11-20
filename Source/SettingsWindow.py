'''
Created on Oct 31, 2011

@author: Carke
'''
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
        if Buttons.Resize(Upload, (130,70)):
            if event.type == MOUSEBUTTONUP :
                #v = raw_input("Filename: ")
                filename = askopenfilename(filetypes=[("All Files","*"),("jpeg","*.jpg")], initialdir=(os.path.dirname("C:\Users")))
                Image1 = Buttons((175,350,104,104),filename,filename)
                v = Image1
        if Buttons.Collision(Back, 195, 68, (300,450,195,68), "images/Back_hover.png", "images/Back_normal.png", 0):
            if event.type == MOUSEBUTTONUP:
                state = 1
        if Buttons.Resize(Bow, (100,100)):
            if event.type == MOUSEBUTTONUP:
                v = Bow
        if Buttons.Resize(Bear, (100,100)):
            if event.type == MOUSEBUTTONUP:
                v = Bear
        if Buttons.Resize(Cake, (100,100)):
            if event.type == MOUSEBUTTONUP:
                v = Cake
        pygame.event.clear()
        Buttons.Resize(Image1, (104,104))
        pygame.display.update()