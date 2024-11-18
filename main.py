import pygame, sys
import platform
from settings import *
from loadingscreen import Load
from pick import Pick

os_name = platform.system()

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('สามตัวบาท')
		self.clock = pygame.time.Clock()
		self.loading = Load()
		self.pick = Pick()
		self.pick_done = [False,0,0]
		self.start = False
		self.pg = 1
		self.delayclick = 0
		self.main_sound = pygame.mixer.Sound("assets/audio/music.mp3")
		self.click_sound = pygame.mixer.Sound("assets/audio/click.mp3")
		self.main_sound.set_volume(0.5)
		self.click_sound.set_volume(1.0)

	def wait(self):
		if not self.pick_done[0]: 
			self.pick_done[0] = True
			self.delayclick = pygame.time.get_ticks()

	def cwait(self):
		if self.pick_done[0]:
			current_time = pygame.time.get_ticks()
			if current_time - self.delayclick >= 1000:
				self.pick_done[0] = False
				
	def run(self):
		self.main_sound.play(-1)
		while True:
			CLOCK.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						if self.loading.button_enter_rc.collidepoint(event.pos) and not self.start:
							self.loading.fading = True
							self.loading.fade_direction = -1
							self.start = True
							self.wait()
						elif self.loading.button_exit_rc.collidepoint(event.pos) and not self.start:
							pygame.quit()
							sys.exit()
						elif self.pick.d1_p.collidepoint(event.pos) and not self.pick_done[0] and not self.pick.status:
							self.click_sound.play()
							self.pick_done = [True,1,1]
							self.pick.status = True
							self.pick.sendstate(self.pick_done)
						elif self.pick.d2_p.collidepoint(event.pos) and not self.pick_done[0] and not self.pick.status:
							self.click_sound.play()
							self.pick_done = [True,2,1]
							self.pick.status = True
							self.pick.sendstate(self.pick_done)
						elif self.pick.d3_p.collidepoint(event.pos) and not self.pick_done[0] and not self.pick.status:
							self.click_sound.play()
							self.pick_done = [True,3,1]
							self.pick.status = True
							self.pick.sendstate(self.pick_done)

			self.cwait()
			self.loading.run()
			if self.loading.pg == 2:
				self.pick.run()
				self.main_sound.stop()
			pygame.display.update()
			pygame.display.flip()
		


if __name__ == '__main__':
	game = Game()
	game.run()
