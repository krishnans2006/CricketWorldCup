# Made by Krishnan Shankar and Shivam Suri
# Enjoy!
# Shivam presents this part.
import pygame

from characters import Player, Bowler

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

W = 800
H = 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Cricket Game")
BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (W, H))
PITCH = pygame.transform.scale(pygame.image.load("pitch.png"), (300, 200))

# Krishna presents this part.
def redraw(win, player):
	win.blit(BG, (0, 0))
	win.blit(PITCH, (250, 400))
	player.update()
	player.draw(win)
	pygame.draw.line(win, (0, 0, 0), (379, 555), (379, 597), 6)
	pygame.draw.line(win, (0, 0, 0), (399, 550), (399, 597), 6)
	pygame.draw.line(win, (0, 0, 0), (419, 555), (419, 597), 6)
	pygame.draw.line(win, (0, 0, 0), (380, 550), (398, 550), 4)
	pygame.draw.line(win, (0, 0, 0), (400, 550), (418, 550), 4)
	pygame.display.flip()

# Shivam presents this part.
def main():
	player = Player(290, 460)
	bowler = Bowler(0, 0)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.swing()
		redraw(win, player)
		clock.tick(30)


if __name__ == "__main__":
	main()
