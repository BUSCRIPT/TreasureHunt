import pygame , sys
import platform
from settings import *


os_name = platform.system()

class Display:
    def __init__(self):
        # General
        self.display_surface = pygame.display.get_surface()
        if os_name == "Windows":
            self.energy_bar_rect = pygame.Rect(200, 940, ENERGY_BAR_WIDTH, BAR_HEIGHT)
            self.images = {
                "logo": ("assets/graphics/icon/logo.png", (1650, 190)),
                "minimap": ("assets/graphics/icon/minimap.png", (1590, 510)),
                "energy": ("assets/graphics/help_notification/energy.png", (1050, 480)),
                "shop": ("assets/graphics/help_notification/shop.png", (1050, 480)),
                "mine": ("assets/graphics/help_notification/mine.png", (1050, 480)),
                "error": ("assets/graphics/help_notification/no.png", (1050, 480)),
                "house": ("assets/graphics/help_notification/house.png", (1050, 480)),
                "level0": ("assets/graphics/level/0.png", (240, 150)),
                "level1": ("assets/graphics/level/1.png", (240, 150)),
                "level2": ("assets/graphics/level/2.png", (240, 150)),
                "level3": ("assets/graphics/level/3.png", (240, 150)),
                "job0": ("assets/graphics/job/0.png", (335, 490)),
                "job1": ("assets/graphics/job/1.png", (335, 490)),
                "job2": ("assets/graphics/job/2.png", (335, 490)),
                "job3": ("assets/graphics/job/3.png", (335, 490)),
                "job4": ("assets/graphics/job/4.png", (335, 490)),
                "job5": ("assets/graphics/job/5.png", (335, 490)),
                "job6": ("assets/graphics/job/6.png", (335, 490)),
                "job7": ("assets/graphics/job/7.png", (335, 490)),
                "job8": ("assets/graphics/job/8.png", (335, 490)),
                "job9": ("assets/graphics/job/9.png", (335, 490)),
                "backpack": ("assets/graphics/backpack/0.png", (1650, 850)),
                "end": ("assets/graphics/bg/end.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 500)),
            }
        elif os_name == "Darwin":
            self.energy_bar_rect = pygame.Rect(30, 1100, ENERGY_BAR_WIDTH, BAR_HEIGHT)
            self.images = {
                "logo": ("assets/graphics/icon/logo.png", (1850, 90)),
                "minimap": ("assets/graphics/icon/minimap.png", (1780, 410)),
                "energy": ("assets/graphics/help_notification/energy.png", (1050, 550)),
                "shop": ("assets/graphics/help_notification/shop.png", (1050, 550)),
                "mine": ("assets/graphics/help_notification/mine.png", (1050, 550)),
                "error": ("assets/graphics/help_notification/no.png", (1050, 550)),
                "house": ("assets/graphics/help_notification/house.png", (1050, 550)),
                "level0": ("assets/graphics/level/0.png", (50, 60)),
                "level1": ("assets/graphics/level/1.png", (50, 60)),
                "level2": ("assets/graphics/level/2.png", (50, 60)),
                "level3": ("assets/graphics/level/3.png", (50, 60)),
                "job0": ("assets/graphics/job/0.png", (150, 530)),
                "job1": ("assets/graphics/job/1.png", (150, 530)),
                "job2": ("assets/graphics/job/2.png", (150, 530)),
                "job3": ("assets/graphics/job/3.png", (150, 530)),
                "job4": ("assets/graphics/job/4.png", (150, 530)),
                "job5": ("assets/graphics/job/5.png", (150, 530)),
                "job6": ("assets/graphics/job/6.png", (150, 530)),
                "job7": ("assets/graphics/job/7.png", (150, 530)),
                "job8": ("assets/graphics/job/8.png", (150, 530)),
                "job9": ("assets/graphics/job/9.png", (150, 530)),
                "backpack": ("assets/graphics/backpack/0.png", (1820, 1020)),
                "end": ("assets/graphics/bg/end_mac.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 500)),
            }
        self.loaded_images = {}
        for name, (path, center) in self.images.items():
            image = pygame.image.load(path).convert_alpha()
            rect = image.get_rect(center=center)
            self.loaded_images[name] = {"image": image, "rect": rect}
    
    def show_level(self, surface, rect, image):
        self.lv = image.copy()
        self.lv.set_alpha(255)
        surface.blit(self.lv, rect)
    
    def show_quest(self, surface, rect, image):
        self.quest = image.copy()
        self.quest.set_alpha(255)
        surface.blit(self.quest, rect)

    def show_backpack(self, surface, rect, image):
        self.bp = image.copy()
        self.bp.set_alpha(255)
        surface.blit(self.bp, rect)
        
    def draw_noti(self, surface, rect, image):
        self.noti = image.copy()
        self.noti.set_alpha(255)
        surface.blit(self.noti, rect)

    def show_bar(self, current, max_amount, bg_rect, color):
        # Draw Background
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # Converting Stats to Pixels
        ratio = current / max_amount 
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # Drawing the Bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        

    def display(self, player):
        self.show_bar(player.energy, player.stats["energy"], self.energy_bar_rect, ENERGY_COLOR)
        self.draw_noti(self.display_surface,self.loaded_images["logo"]["rect"],self.loaded_images["logo"]["image"])
        self.draw_noti(self.display_surface,self.loaded_images["minimap"]["rect"],self.loaded_images["minimap"]["image"])
        self.show_backpack(self.display_surface,self.loaded_images["backpack"]["rect"],self.loaded_images["backpack"]["image"])
        self.show_quest(self.display_surface,self.loaded_images[f"job{player.job}"]["rect"],self.loaded_images[f"job{player.job}"]["image"])
        if player.level == 0:
            self.show_level(self.display_surface, self.loaded_images["level0"]["rect"], self.loaded_images["level0"]["image"])
        elif player.level == 1:
            self.show_level(self.display_surface, self.loaded_images["level1"]["rect"], self.loaded_images["level1"]["image"])
        elif player.level == 2:
            self.show_level(self.display_surface, self.loaded_images["level2"]["rect"], self.loaded_images["level2"]["image"])
        elif player.level == 3:
            self.show_level(self.display_surface, self.loaded_images["level3"]["rect"], self.loaded_images["level3"]["image"])
        if player.job == 9:
            self.draw_noti(self.display_surface, self.loaded_images["end"]["rect"], self.loaded_images["end"]["image"])
            # sys.exit()
        
    def help_notification(self,nb,error,error_level,error_house):
        if nb == 'energy':
            self.draw_noti(self.display_surface, self.loaded_images["energy"]["rect"], self.loaded_images["energy"]["image"])
        elif nb == 'shop':
            if error_level:
                self.draw_noti(self.display_surface, self.loaded_images["error"]["rect"], self.loaded_images["error"]["image"])
            else:
                self.draw_noti(self.display_surface, self.loaded_images["shop"]["rect"], self.loaded_images["shop"]["image"])
        elif nb == 'house':
            if not error_house:
                self.draw_noti(self.display_surface, self.loaded_images["error"]["rect"], self.loaded_images["error"]["image"])
            else:
                self.draw_noti(self.display_surface, self.loaded_images["house"]["rect"], self.loaded_images["house"]["image"])
        elif nb == 'mine':
            if error:
                self.draw_noti(self.display_surface, self.loaded_images["error"]["rect"], self.loaded_images["error"]["image"])
                