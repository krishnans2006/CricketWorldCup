# Shivam does this part.
from pygame.transform import scale

from pygame.image import load

class Player:
	imgs = [
		scale(load("player1.png"), (128, 128)),
		scale(load("player2.png"), (128, 128)),
		scale(load("player3.png"), (128, 128))
	]

    # Krishna does this part.
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.swinging = False
		self.swing_cnt = None
		self.img = self.imgs[0]
		self.swing_time = 30

	def update(self):
		if self.swinging:
			self.swing_cnt += 1
		if self.swing_cnt == self.swing_time / 2:
			self.img = self.imgs[2]
		if self.swing_cnt == self.swing_time:
			self.stop_swing()

	def draw(self, win):
		win.blit(self.img, (self.x, self.y))

	def swing(self):
		if not self.swinging:
			self.swinging = True
			self.swing_cnt = 1
			self.img = self.imgs[1]
			print("Swing!")

	def stop_swing(self):
		self.swinging = False
		self.swing_cnt = 0
		self.img = self.imgs[0]

# Shivam does this part.
class Bowler:
	imgs = [
		load("bowler1.png"),
		load("bowler2.png")
	]
class Ball:
	imgs = [
		 load("ball1.png")
		 load("ball2.png")
	]