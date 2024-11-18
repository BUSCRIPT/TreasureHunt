import pygame
import platform

os_name = platform.system()

if os_name == "Windows":
	SCREEN_WIDTH = 1920
	SCREEN_HEIGHT = 1080
	BAR_HEIGHT = 15
	ENERGY_BAR_WIDTH = 1520
elif os_name == "Darwin":
	SCREEN_WIDTH = 1920
	SCREEN_HEIGHT = 1200
	BAR_HEIGHT = 15
	ENERGY_BAR_WIDTH = 1870
	
TILE_SIZE = 64


ENERGY_COLOR = "#fff000"

UI_BG_COLOR = "#222222"
UI_BORDER_COLOR = "#111111"

CLOCK = pygame.time.Clock()

HITBOX_OFFSET = {
	"player": -26,
	"object": -40,
	"grass": -10,
	"invisible": 0
}