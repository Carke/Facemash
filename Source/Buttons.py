import pygame
pygame.init()
MainMenu = pygame.display.set_mode([700,700])
AboutMenu = pygame.display.set_mode([500,500])
InstructionsMenu = pygame.display.set_mode([500,500])
SettingsMenu = pygame.display.set_mode([500,500])
#v = raw_input("Filename: ")

class Buttons(pygame.sprite.Sprite):
    def __init__(self, filename, location, surface):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        surface.blit(self.image,self)
class Buttons2(pygame.sprite.Sprite):
    def __init__(self, filename, location, surface):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (104,56))

        self.rect = self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        surface.blit(self.image,self)
class Buttons3(pygame.sprite.Sprite):
    def __init__(self, filename, location, surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (511,141))

        self.rect = self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        InstructionsMenu.blit(self.image,self)
        
AboutButtoninitial = Buttons("images/about_normal.png", (350,430), MainMenu)
PlayButtoninitial = Buttons("images/play_normal.png", (80,225), MainMenu)
InstructionsButtoninitial = Buttons("images/learn_normal.png", (350,225), MainMenu)
SettingButtoninitial = Buttons("images/settings_normal.png", (55,430), MainMenu)
Logo = Buttons("images/logo_normal.png", (50,25), MainMenu)
AboutButtonHover = Buttons("images/about_hover.png", (350,430), MainMenu)
PlayButtonHover = Buttons("images/play_hover.png", (80,225), MainMenu)
InstructionsButtonHover = Buttons("images/learn_hover.png", (350,225), MainMenu)
SettingButtonHover = Buttons("images/settings_hover.png", (55,430), MainMenu)
LogoHover = Buttons("images/logo_hover.png", (50,25), MainMenu)
AboutTitleText = Buttons("images/AboutTitle_normal.png", (110,0), AboutMenu)
InstructionsTitleText = Buttons3("images/InstructionsTitle_normal.png", (0,0), InstructionsMenu)
TitleText = Buttons("images/SettingsTitle_normal.png", (100,0), SettingsMenu)
AudioText = Buttons("images/audio_normal.png", (25,140), SettingsMenu)
AudioON = Buttons2("images/ON_normal.png", (240,150), SettingsMenu)
AudioSETON = Buttons2("images/ON_hover.png", (240,150), SettingsMenu)
AudioOFF = Buttons2("images/OFF_normal.png", (350,150), SettingsMenu)
AudioSETOFF = Buttons2("images/OFF_hover.png", (350,150), SettingsMenu)
#Image1 = Buttons(v,(300,100),SettingsMenu)
