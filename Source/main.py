#
#
#	This is the start. Let's make something great.
#
#

import pygame, cv
from camera import *
from pygame.locals import *
# import settings
# import play
# import learn

class Game():

	def __init__(self):
		pygame.init()
		screen = pygame.display.set_mode(pygame.FULLSCREEN)
		pygame.display.set_caption('Facemash')
	def event(self, event):
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

def main():
	setting = 0
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	image = Camera()
	expression = Expression()
	while setting == 0:
		expression.choose()
		is_correct = False
		lobster = pygame.font.match_font('Lobster 1.4,')
		font = pygame.font.Font(lobster, 36)
		text = font.render(expression.expression + " on the " + expression.side, 1, (255,255,255))
		textpos = text.get_rect()
		textpos = text.get_rect(centerx=screen.get_width()/2)
		while not is_correct:
			is_correct = image.detectExpression(expression)
			#print expression.score
			image.render(text, textpos)
			pygame.display.flip()
		event = pygame.event.poll()
		pygame.display.flip()
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			setting = 1


# Run the main program now.			
if __name__ == "__main__":
	main()

