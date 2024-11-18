import pygame, sys , platform
from settings import *
from map import Map

os_name = platform.system()

class Pick:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.d1 = pygame.image.load('assets/graphics/digger/1.png').convert_alpha()
		self.d1_s = pygame.image.load('assets/graphics/digger/1s.png').convert_alpha()
		self.d2 = pygame.image.load('assets/graphics/digger/2.png').convert_alpha()
		self.d2_s = pygame.image.load('assets/graphics/digger/2s.png').convert_alpha()
		self.d3 = pygame.image.load('assets/graphics/digger/3.png').convert_alpha()
		self.d3_s = pygame.image.load('assets/graphics/digger/3s.png').convert_alpha()
		if os_name == 'Windows':
			self.top = 480
			self.l1 = 1350
			self.l2 = 950
			self.l3 = 550
		elif os_name == 'Darwin':
			self.top = 550
			self.l1 = 1320
			self.l2 = 920
			self.l3 = 520
		self.d1_p = self.d1.get_rect(center=(SCREEN_WIDTH - self.l1, SCREEN_HEIGHT // 2),top=self.top) 
		self.d2_p = self.d2.get_rect(center=(SCREEN_WIDTH - self.l2, SCREEN_HEIGHT // 2),top=self.top) 
		self.d3_p = self.d2.get_rect(center=(SCREEN_WIDTH - self.l3, SCREEN_HEIGHT // 2),top=self.top) 
		self.c1,self.c2,self.c3 = self.d1,self.d2,self.d3
		self.status = False
		self.map = Map()

	def update_image(self, mouse_state, normal_image, hover_image):
		if mouse_state:
			image = hover_image
			image.set_alpha(200)
		else:
			image = normal_image
			image.set_alpha(255)
		return image

	def run(self):
		
		self.display_surface.blit(self.c1, self.d1_p)
		self.display_surface.blit(self.c2, self.d2_p)
		self.display_surface.blit(self.c3, self.d3_p)

		mp = pygame.mouse.get_pos()
		self.mouse_d1 = self.d1_p.collidepoint(mp)
		self.mouse_d2 = self.d2_p.collidepoint(mp)
		self.mouse_d3 = self.d3_p.collidepoint(mp)

		self.c1 = self.update_image(self.mouse_d1, self.d1, self.d1_s)
		self.c2 = self.update_image(self.mouse_d2, self.d2, self.d2_s)
		self.c3 = self.update_image(self.mouse_d3, self.d3, self.d3_s)
	
		if self.status:
			self.display_surface.fill('#71a0ee')
			self.map.run()
	
	def sendstate(self,state):
		self.map.set_state(state)


		







		
