# Shivam does this part.
from pygame.image import load
from pygame.transform import scale


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
		scale(load("bowler1.png"), (128, 128)),
		scale(load("bowler2.png"), (128, 128))
	]

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.bowling = False
		self.bowl_cnt = None
		self.img = self.imgs[0]
		self.bowl_time = 30

	def update(self):
		if self.bowling:
			self.bowl_cnt += 1
		if self.bowl_cnt == self.bowl_time // 2:
			self.img = self.imgs[1]
		if self.bowl_cnt == self.bowl_time:
			self.img = self.imgs[0]

	def bowl(self):
		if not self.bowling:
			self.bowling = True
			self.bowl_cnt = 1
			print("Bowl!")

	def draw(self, win):
		win.blit(self.img, (self.x, self.y))

class Ball:
	imgs = [scale(load("ball1.png"), (64,64)), scale(load("ball2.png"), (64, 64)]
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = self.imgs[0]

	def draw(self, win):
		win.blit(self.img, (self.x, self.y))