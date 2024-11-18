import pygame, sys
from helper import import_folder
from settings import *
from entity import Entity



class Player(Entity):
	def __init__(self, pos, groups, obstacle_sprites, pick_done):
		super().__init__(groups)
		self.pick_done = pick_done

		self.load_player_assests()
		self.rect = self.player.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(-6, HITBOX_OFFSET["player"])
		self.stats = {"energy": 60, "speed": 5, "level":0 , "done":1 , "job":0, "store":None, "complete":False}
		self.energy = self.stats["energy"]
		self.level = self.stats["level"]
		self.done = self.stats["done"]
		self.job = self.stats["job"]
		self.store = self.stats["store"]
		self.complete = self.stats["complete"]
		self.import_player_assets()
		self.status = "down"
		self.speed = 5

		self.obstacle_sprites = obstacle_sprites

		self.hit = False

		self.attack_sound = pygame.mixer.Sound("assets/audio/attack.wav")
		self.attack_sound.set_volume(0.8)
		self.running_sound = pygame.mixer.Sound("assets/audio/running.wav")
		self.running_sound.set_volume(1.0)
	
	def load_player_assests(self):
		self.player = pygame.image.load("assets/graphics/journey/invisible_entity.png").convert_alpha()

	def import_player_assets(self):
		if self.pick_done[1] == 1:
			character_path = "assets/graphics/journey/1_1/"
		elif self.pick_done[1] == 2:
			character_path = "assets/graphics/journey/2_1/"
		elif self.pick_done[1] == 3:
			character_path = "assets/graphics/journey/3_1/"
		self.animations = {
			"up": [], "down": [], "left": [], "right": [],
			"right_idle": [], "left_idle": [], "up_idle": [], "down_idle":[],
			"right_attack": [], "left_attack": [], "up_attack": [], "down_attack":[]
        }
		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)
                  
	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.direction.y = -1
			self.status = "up"
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
			self.status = "down"
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
			self.status = "right"
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.status = "left"
		else:
			self.direction.x = 0
		
		if keys [pygame.K_RETURN] and not self.energy <= 0:
			self.hit = True
			self.status = "right"
			self.attack_sound.play()
		
		if keys[pygame.K_LSHIFT]:
			if self.energy <= 0:
				self.stats["speed"] = 5
			if self.energy >= 0:
				self.stats["speed"] = 10
				self.energy = self.energy - 0.05
				self.running_sound.play(-1)
		else:
			self.stats["speed"] = 5 
			self.running_sound.stop()

	def get_status(self):
		if self.direction.x == 0 and self.direction.y == 0:
			if not "idle" in self.status:
				self.status = self.status + "_idle"
		if self.hit:
			self.direction.x = 0
			self.direction.y = 0
			if not "attack" in self.status:
				if "idle" in self.status:
					self.status = self.status.replace("_idle", "_attack")
				else:
					self.status = self.status + "_attack"
			else:
				if "attack" in self.status:
					self.status = self.status.replace("_attack", "")
					self.hit = False

	def animate(self):
		animation = self.animations[self.status]

        # Loop over the frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

        # Set the image
		self.player = animation[int(self.frame_index)]
		self.rect = self.player.get_rect(center = self.hitbox.center)

	def update(self):
		self.input()
		self.get_status()
		self.animate()
		self.move(self.stats["speed"])

