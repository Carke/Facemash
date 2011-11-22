#imports and inits
import pygame, os
from pygame.locals import *
MainMenu = pygame.display.set_mode([700,700])
AboutMenu = pygame.display.set_mode([500,550])
InstructionsMenu = pygame.display.set_mode([500,550])
SettingsMenu = pygame.display.set_mode([500,550])
pygame.init()
x1=0
y1=0
for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            x1=event.pos[0] 
            y1=event.pos[1]
#defining default variables
state = 0
x = 0
y = 0
#exits the window or game
def Quit():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 1
#detects mouseover motion
def MouseOver():
    global x1
    global y1
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            x1=event.pos[0] 
            y1=event.pos[1]
#buttons class that all objects are a part of
class Buttons(pygame.sprite.Sprite):
    def __init__(self, location, initial, hover):
        pygame.sprite.Sprite.__init__(self)
        # defines initial image and hover state with transparencies
        try:
            self.image = pygame.image.load(initial).convert_alpha()
        except:
            self.image = pygame.image.load("images/blank.png").convert_alpha()
        self.image = pygame.image.load(initial).convert_alpha()
        self.hover = pygame.image.load(hover).convert_alpha()
        # defines Rect attributes for sprite
        self.Rect = pygame.Rect((location))

        self.rect = self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        pygame.display.get_surface().blit(self.image,self)
    #method for handling collision
    def Collision(self):
        MouseOver()
        global x
        if self.Rect.collidepoint((x1,y1)):
            pygame.display.get_surface().blit(self.hover,self)
#            while x < 3 :
#                length = length*1.01
#                width = width*1.01
#                self.hover = pygame.transform.scale(self.hover, (length, width))
#                pygame.display.get_surface().blit(self.hover, self)
#                pygame.display.update()
#                pygame.time.wait(50)
#                x=x+1
            return True
    #method for objects that need to be resized and their collisions
    def Resize(self, dimensions):
        self.image = pygame.transform.scale(self.image, dimensions)
        self.hover = pygame.transform.scale(self.hover, dimensions)
        MouseOver()
        if self.Rect.collidepoint((x1,y1)) :
            pygame.display.get_surface().blit(self.hover,self)
            Quit()
            return True
#initial state of all uploaded objects with the exception of user uploaded ones
TitleText = Buttons((100,0,0,0),"images/SettingsTitle_normal.png", "images/SettingsTitle_normal.png")
AudioText = Buttons((25,140,0,0),"images/audio_normal.png", "images/audio_normal.png")
Logo = Buttons((50,25,0,0),"images/logo_normal.png", "images/logo_hover.png")
AboutTitleText = Buttons((110,0,0,0),"images/AboutTitle_normal.png", "images/AboutTitle_normal.png")
AboutButton = Buttons((350,430,280,70), "images/about_normal.png", "images/about_hover.png")
PlayButton = Buttons((100,225,260,140),"images/play_normal.png", "images/play_hover.png")
InstructionsButton = Buttons((375,225,260,140),"images/learn_normal.png", "images/learn_hover.png")
SettingButton = Buttons((55,430, 280,70),"images/settings_normal.png", "images/settings_hover.png")
InstructionsTitleText = Buttons((0,0,0,0),"images/InstructionsTitle_normal.png","images/InstructionsTitle_normal.png")
AudioON = Buttons((240,150,104,56),"images/ON_normal.png", "images/ON_hover.png")
AudioOFF = Buttons((350,150,104,56),"images/OFF_normal.png", "images/OFF_hover.png")
Upload = Buttons((30,375,130,70), "images/Upload_normal.png", "images/Upload_hover.png")
Back = Buttons((25,500,195,35), "images/Back_normal.png", "images/Back_hover.png")
Bear = Buttons((75,250,100,100), "Assets/Stickers/bear.png", "Assets/Stickers/bear.png")
Bow = Buttons((200,250,100,100), "Assets/Stickers/bow.png", "Assets/Stickers/bow.png")
Cake = Buttons((325,250,100,100), "Assets/Stickers/cake.png", "Assets/Stickers/cake.png")
Exit = Buttons((275,500,130,70), "images/Exit_normal.png", "images/Exit_hover.png")
AboutText = Buttons((100,140,0,0), "images/AboutText.png", "images/AboutText.png")
