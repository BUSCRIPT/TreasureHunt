import pygame
import platform
from settings import *
from journey import Player
from helper import import_folder

os_name = platform.system()

class Dig:
    def __init__(self):
        
        # General
        self.display_surface = pygame.display.get_surface()
        self.start = False
        self.current_mine = {"1": 0, "2": 0, "3":0}
        self.mine_completed = {"1": False, "2": False, "3": False}
        self.press_count = 0
        self.press_lv = 0 
        self.error_house = False
        self.load_backpack = {1:pygame.image.load('assets/graphics/backpack/1_0.png').convert_alpha(),
                              2:pygame.image.load('assets/graphics/backpack/2_0.png').convert_alpha(),
                              3:pygame.image.load('assets/graphics/backpack/3_0.png').convert_alpha(),
                              4:pygame.image.load('assets/graphics/backpack/4_0.png').convert_alpha()}
        if os_name == "Windows":
            self.bt = 410
            self.wm = 1595
            self.hm = 795
            self.end = pygame.image.load('assets/graphics/bg/end.png').convert_alpha()
        elif os_name == "Darwin":
            self.bt = 470
            self.wm = 1765
            self.hm = 965
            self.end = pygame.image.load('assets/graphics/bg/end_mac.png').convert_alpha()
    def load_mine_images(self, level):
        images = []
        for i in range(0, 12):
            image_path = f"assets/graphics/mine/{level}/{level}_{i}.png"
            surface = pygame.image.load(image_path).convert_alpha()
            images.append(surface)
        return images

    def start_level(self, pl):
        self.load_mine = self.load_mine_images(pl.level)
        self.total_mine = len(self.load_mine)

    def display_mines(self,pl):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and not self.delaypress and not self.current_mine[str(pl.level)] == self.total_mine and pl.store == False and not pl.energy <= 0:
            self.delaypress = True
            self.press_count += 1
            # self.press_lv = 1 if pl.level == 1 else 1 if pl.level == 2 else 1 if pl.level == 3 else self.press_lv
            self.press_lv = pl.level
            if self.press_count == self.press_lv:
                if self.current_mine[str(pl.level)] > 12:
                    self.current_mine[str(pl.level)] = 12
                self.current_mine[str(pl.level)] += 1
                self.press_count = 0
        if not keys[pygame.K_RETURN]:
            self.delaypress = False
        if self.current_mine[str(pl.level)] < self.total_mine:
            self.display_surface.blit(self.load_mine[self.current_mine[str(pl.level)]], (985, self.bt))
        if self.current_mine[str(pl.level)] == self.total_mine:
            if pl.level < 3:
                pl.done = pl.level + 1
        if self.current_mine["1"] == self.total_mine and not self.mine_completed["1"]:
            pl.job = 2
            pl.store = False
            self.mine_completed["1"] = True
            self.error_house = True
        if self.current_mine["2"] == self.total_mine and not self.mine_completed["2"]:
            pl.job = 5
            pl.store = False
            self.mine_completed["2"] = True
            self.error_house = True
        if self.current_mine["3"] == self.total_mine and not self.mine_completed["3"]:
            pl.job = 8
            pl.complete = True
            self.mine_completed["3"] = True
            self.error_house = True
            

    def display_backpack(self, pl):
        if str(pl.level) in self.current_mine and not pl.store:
            mine_count = self.current_mine[str(pl.level)]
            alpha_values = {
                (1, 1): 10,
                (2, 3): 30,
                (4, 5): 50,
                (6, 7): 100,
                (8, 9): 150,
                (10, 12): 255
            }
            for (low, high), alpha in alpha_values.items():
                if low <= mine_count <= high:
                    if not pl.complete:
                        self.load_backpack[pl.level].set_alpha(alpha)
                        self.display_surface.blit(self.load_backpack[pl.level], (self.wm, self.hm))
                    else:
                        self.load_backpack[4].set_alpha(alpha)
                        self.display_surface.blit(self.load_backpack[4], (self.wm-3, self.hm-5))
                    break


    def run(self,pl):
        if self.start:
            if self.current_mine[str(pl.level)] == 0:
                self.start_level(pl)
            self.display_mines(pl)

