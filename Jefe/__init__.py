import pygame
#from loader import 
# Clase base
from Ship import Ship
# Necesarios para el funcionameinto
from Laser import Laser


import random

class Jefe(Ship):

    self.dificultad = random.randrange(20, 50)

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    
    def shoot(self):
        if self.cool_down_counter == 0:
            # spawnea el saler en la posicion de la nave
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
        
    def bullet_hell(self):
        """
        Esto recibe una input aleatoria y un gran contador
        """
        if self.bullet_hell_cool_down_counter == 0:
            for i in range(self.dificultad):
                laser = Laser(self.x-20, self.y, self.laser_img)
                self.lasers.append(laser)
