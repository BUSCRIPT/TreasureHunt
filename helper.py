from csv import reader
import os
from os import walk
import pygame

def import_csv_layout(path): 
    
    tmap = []

    with open(path) as level_map:
        layout = reader(level_map, delimiter = ",")

        for row in layout:
            tmap.append(list(row))
        
        return tmap


def import_folder(path):
    surface = []
    
    for _, __, img_files in walk(path):
        img_files.sort()
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface.append(image_surf)
    return surface