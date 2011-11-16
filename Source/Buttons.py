import pygame
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

        self.rect = self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        pygame.display.get_surface().blit(self.image,self)
    def Collision(self):
        MouseOver()
        if self.Rect.collidepoint((x1,y1)) :
            pygame.display.get_surface().blit(self.hover,self)
            Quit()
            return True
        
class Buttons2(pygame.sprite.Sprite):
    def __init__(self, location, initial, hover):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(initial).convert_alpha()
        self.image = pygame.transform.scale(self.image, (104,56))
        self.hover = pygame.image.load(hover).convert_alpha()
        self.hover = pygame.transform.scale(self.hover, (104,56))
        self.Rect = pygame.Rect((location))


        self.rect = self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        pygame.display.get_surface().blit(self.image,self)
    def Collision(self):
        MouseOver()
        if self.Rect.collidepoint((x1,y1)) :
            pygame.display.get_surface().blit(self.hover,self)
            Quit()
            return True
            
class Buttons3(pygame.sprite.Sprite):
    def __init__(self, filename, location, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (511,141))

        self.rect = self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        pygame.display.get_surface().blit(self.image,self)
        
TitleText = Buttons((100,0,0,0),"images/SettingsTitle_normal.png", "images/SettingsTitle_normal.png")
AudioText = Buttons((25,140,0,0),"images/audio_normal.png", "images/audio_normal.png")
Logo = Buttons((50,25,0,0),"images/logo_normal.png", "images/logo_hover.png")
AboutTitleText = Buttons((110,0,0,0),"images/AboutTitle_normal.png", "images/AboutTitle_normal.png")
AboutButton = Buttons((350,430,280,70), "images/about_normal.png", "images/about_hover.png")
PlayButton = Buttons((100,225,260,140),"images/play_normal.png", "images/play_hover.png")
InstructionsButton = Buttons((375,225,260,140),"images/learn_normal.png", "images/learn_hover.png")
SettingButton = Buttons((55,430, 280,70),"images/settings_normal.png", "images/settings_hover.png")
InstructionsTitleText = Buttons3("images/InstructionsTitle_normal.png",(0,0),)
AudioON = Buttons2((240,150,104,56),"images/ON_normal.png", "images/ON_hover.png")
AudioOFF = Buttons2((350,150,104,56),"images/OFF_normal.png", "images/OFF_hover.png")
#Image1 = Buttons(("C:/Users/Carke ",v,),(300,100),SettingsMenu)
