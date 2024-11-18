import pygame, sys
from settings import *
from tile import Tile
from helper import *
from journey import Player
from display import Display
from dig import Dig
from random import choice, randint
class Map:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.visible_sprites = ShowMap()
		self.obstacle_sprites = pygame.sprite.Group()
		self.state = None
		self.ui = Display()

	def set_state(self, state):
		self.state = state  
		self.create_map()   

	def create_map(self):
        
		layouts = {
            "boundary": import_csv_layout("assets/data/map/map_FloorBlocks.csv"),
            "grass": import_csv_layout("assets/data/map/map_Grass.csv"),
            "object": import_csv_layout("assets/data/map/map_Objects.csv"),
            "entities": import_csv_layout("assets/data/map/map_Entities.csv")
        }
            
		graphics = {
            "grass": import_folder("assets/data/grass/"),
            "objects": import_folder("assets/data/objects/")
        }

		for style, layout in layouts.items():
			for row_index, row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != "-1":
						x = col_index * TILE_SIZE
						y = row_index * TILE_SIZE
						if style == "boundary":
							Tile((x, y), [self.obstacle_sprites], "invisible")
						if style == "grass":
							random_grass_image = choice(graphics["grass"])
							Tile((x, y), [self.visible_sprites, self.obstacle_sprites],"grass", random_grass_image)
                        
						if style == "object":
							surf = graphics["objects"][int(col)]
							Tile((x, y), [self.visible_sprites, self.obstacle_sprites], "object", surf)
						if style == "entities":
							if col == "394":
								self.pl = Player((x, y),[self.visible_sprites],self.obstacle_sprites,self.state)

	def run(self):
		self.visible_sprites.custom_draw(self.pl)
		self.visible_sprites.update()
		
		self.ui.display(self.pl)
		
		

class ShowMap(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()
		
		self.error = False
		self.error_level = False

		# Creating the floor
		self.floor = pygame.image.load("assets/graphics/world/ground.png").convert()
		self.floor_rc = self.floor.get_rect(topleft = (0, 0))

		self.point = [[459, 369],[1656,177],[2941,2417],[1312,2355]]
		self.nb = None

		self.ui = Display()
		self.dig = Dig()

	def custom_draw(self,player):

		# Getting the offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height
		

		# Drawing the floor
		floor_offset_pos = self.floor_rc.topleft - self.offset
		self.display_surface.blit(self.floor, floor_offset_pos)
		
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.player, offset_pos)
		

		if (player.level == 0 and player.done == 1) or (player.level == 1 and player.done == 2) or (player.level == 2 and player.done == 3):
			self.error = True
		else:
			self.error = False

		self.check_player(player)
	
	def check_player(self,player):
		keys = pygame.key.get_pressed()
		player_position = pygame.math.Vector2(player.rect.topleft)
		self.dig.display_backpack(player)
		if player_position.distance_to(self.point[0]) <= 100:
			self.nb = 'energy'
		elif player_position.distance_to(self.point[1]) <= 100:
			self.nb = 'shop'
		elif player_position.distance_to(self.point[2]) <= 100:
			self.nb = 'mine'
		elif player_position.distance_to(self.point[3]) <= 300:
			self.nb = 'house'
		else:
			self.nb = None
		
		
		if self.nb == 'energy':
			if keys[pygame.K_e]:
				if player.energy >= 60:
						player.energy = 60
				if player.energy < 60:
					player.energy = player.energy + 0.25
		elif self.nb == 'shop':
			if keys[pygame.K_e]:
				if player.done == 1:
					player.level = 1
					player.job = 1
					player.store = False
					# player.complete = True
					self.error_level = True
				elif player.done == 2:
					if player.store:
						player.level = 2
						player.job = 4
						player.store = False
						self.error_level = True
					else:
						self.error_level = True
				elif player.done == 3:
					if player.store:
						player.level = 3
						player.job = 7
						player.store = False
						self.error_level = True
					else:
						self.error_level = True
		elif self.nb == 'mine':
			if not self.error:
				self.dig.start = True
				self.dig.run(player)
		elif self.nb == 'house':
			if keys[pygame.K_e]:
				if player.store == False:
					if player.done == 2:
						if player.level == 1:
							player.job = 3
							player.store = True
							self.error_level = False
							self.dig.error_house = False
					if player.done == 3:
						if player.level == 2:
							player.job = 6
							player.store = True
							self.error_level = False
							self.dig.error_house = False
					if player.complete:
						player.job = 9
		if self.nb == 'energy' or self.nb == 'shop' or self.nb == 'mine' or self.nb == "house":
			self.ui.help_notification(self.nb,self.error,self.error_level,self.dig.error_house)

	
	



		

