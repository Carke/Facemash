import pygame, os
from pygame.locals import *
MainMenu = pygame.display.set_mode([700,700])
AboutMenu = pygame.display.set_mode([500,500])
InstructionsMenu = pygame.display.set_mode([500,500])
SettingsMenu = pygame.display.set_mode([500,500])
pygame.init()
x1=0
y1=0
for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            x1=event.pos[0] 
            y1=event.pos[1]
#v = raw_input("Filename: ")
state = 0
x = 0
y = 0
identifier = 0
def Quit():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state = 1
def MouseOver():
    global x1
    global y1
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            x1=event.pos[0] 
            y1=event.pos[1]
        
class Buttons(pygame.sprite.Sprite):
    def __init__(self, location, initial, hover):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(initial).convert_alpha()
        self.hover = pygame.image.load(hover).convert_alpha()
        self.Rect = pygame.Rect((location))
        self.image2 = self.image

        self.rect = self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        pygame.display.get_surface().blit(self.image,self)
    def Collision(self, length, width, location, hover, initial, identifier):
        MouseOver()
        global x
        global y
        if self.Rect.collidepoint((x1,y1)) == False and identifier == 1:
            x=0
            self.hover = pygame.image.load(hover).convert_alpha()
            while y < 3 :
                    length = length*0.98
                    width = width*0.98
                    self.image = pygame.transform.scale(self.image, (length, width))
                    pygame.display.get_surface().blit(self.image, self)
                    pygame.display.update()
                    pygame.time.wait(50)
                    print y
                    y=y+1
            identifier = 0
        if self.Rect.collidepoint((x1,y1)):
            identifier = 1
            if identifier == 1:
                y = 0
                pygame.draw.rect(pygame.display.get_surface(), (111,159,225), location)
                pygame.display.get_surface().blit(self.hover,self)
                self.image2 = pygame.image.load(initial).convert_alpha
                while x < 3 :
                    length = length*1.01
                    width = width*1.01
                    self.hover = pygame.transform.scale(self.hover, (length, width))
                    pygame.display.get_surface().blit(self.hover, self)
                    pygame.display.update()
                    pygame.time.wait(50)
                    print x
                    x=x+1
    def Resize(self, dimensions):
        self.image = pygame.transform.scale(self.image, dimensions)
        self.hover = pygame.transform.scale(self.hover, (104,56))
        MouseOver()
        if self.Rect.collidepoint((x1,y1)) :
            pygame.display.get_surface().blit(self.hover,self)
            Quit()
            return True
        
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
#Image1 = Buttons((0,0,0,0),os.path.dirname(os.getcwd())+v,os.path.dirname(os.getcwd())+v)
