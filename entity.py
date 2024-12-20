import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed
        self.collision("Horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("Vertical")
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == "Horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Moving Right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Moving Left
                        self.hitbox.left = sprite.hitbox.right
                        
        if direction == "Vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Moving Down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Moving Up
                        self.hitbox.top = sprite.hitbox.bottom