import pygame
import platform
from settings import *
os_name = platform.system()
class Load:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		if os_name == "Windows":
			self.bg = [pygame.image.load('assets/graphics/bg/first.png').convert(),pygame.image.load('assets/graphics/bg/sec.png').convert(),]
			self.top = 500
		elif os_name == "Darwin":
			self.bg = [pygame.image.load('assets/graphics/bg/first_mac.png').convert(),pygame.image.load('assets/graphics/bg/sec_mac.png').convert(),]
			self.top = 560
		self.bg_index = 0
		self.fade_direction = -1
		self.fading = False
		self.alpha = 255
		self.button_enter = pygame.image.load('assets/graphics/button/enter.png').convert_alpha()
		self.button_exit = pygame.image.load('assets/graphics/button/exit.png').convert_alpha()
		self.button_enter_rc = self.button_enter.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),top=self.top) 
		self.button_exit_rc = self.button_exit.get_rect(center=(SCREEN_WIDTH - 280, SCREEN_HEIGHT - 150))
		self.bv = True
		self.pg = 1
		self.enter_alpha = 255
		self.exit_alpha = 255

	def draw_button(self, surface, rect, image, alpha):
		self.button_surface = image.copy()
		self.button_surface.set_alpha(alpha)
		surface.blit(self.button_surface, rect)
	
	def fade(self, direction):
		self.alpha += 5 * direction
		if self.alpha <= 0:
			self.alpha = 0
			return True
		if self.alpha >= 255: 
			self.alpha = 255
			return False 
		return None 	

	def run(self):
		if self.fading:
			if self.fade_direction == -1:
				fdo = self.fade(-1)
				if fdo:
					self.bg_index = (self.bg_index + 1) % len(self.bg)
					self.fade_direction = 1
			
					self.pg = 2
			elif self.fade_direction == 1:
				fdi = self.fade(1)
				if fdi:
					self.fading = False
		self.current_bg = self.bg[self.bg_index]
		self.current_bg.set_alpha(self.alpha)
		self.display_surface.blit(self.current_bg, (0, 0))

		mp = pygame.mouse.get_pos()
		self.mouse_hover_enter = self.button_enter_rc.collidepoint(mp)

		self.mouse_hover_exit = self.button_exit_rc.collidepoint(mp)

		if self.fading:
			if self.enter_alpha > 0:
				self.enter_alpha -= 5
			if self.enter_alpha <= 0:
				self.enter_alpha = 0
				self.bv = False 
		else:
			if self.mouse_hover_enter:
				self.enter_alpha = 200
			else:
				self.enter_alpha = 255

			if self.mouse_hover_exit:
				self.exit_alpha = 200
			else:
				self.exit_alpha = 255

		if self.bv:
			self.draw_button(self.display_surface, self.button_enter_rc, self.button_enter, self.enter_alpha)
			self.draw_button(self.display_surface, self.button_exit_rc, self.button_exit, self.exit_alpha)
		
