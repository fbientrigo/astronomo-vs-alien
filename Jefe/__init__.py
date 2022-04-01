import pygame
#from loader import 
# Clase base
from Ship import Ship
# Necesarios para el funcionameinto
from Laser import Laser

from loader import RED_SPACE_SHIP, GREEN_SPACE_SHIP, BLUE_SPACE_SHIP, YELLOW_SPACE_SHIP, RED_LASER, GREEN_LASER, BLUE_LASER, YELLOW_LASER, BG
from loader import HORROR_HEAD, HORROR_EYE, HORROR_LEFT_ARM, HORROR_RIGHT_ARM, MECHA_EYE, MECHA_ARM, MECHA_HEAD, METROID_HEAD

import random

horror = {
    'head': HORROR_HEAD, 'left': HORROR_LEFT_ARM, 'right': HORROR_RIGHT_ARM, 'eye': HORROR_EYE
}

mecha = {
    'head': MECHA_HEAD, 'eye': MECHA_EYE, 'left': MECHA_ARM, 'right': MECHA_ARM
}

metroid = {
    'head': METROID_HEAD, 'left': METROID_HEAD, 'right': METROID_HEAD, 'eye': METROID_HEAD
}


class Jefe(Ship):


    def __init__(self, x, y, tipo, parte, health=200):
        """
        parte: {head, left, right, eye}
        tipo: {horror, mecha, metroid}
        """
        super().__init__(x, y, health)

        self.dificultad = random.randrange(20, 50)

        # ZONA DE CONFIG 
        if tipo == "HORROR":
            self.ship_img = horror[parte]
        elif tipo == "MECHA":
            self.ship_img = horror[parte]
        else: #metroid es el tipo default
            self.ship_img = horror[parte]

        self.laser_img = RED_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)

    
    def shoot(self):
        if self.cool_down_counter == 0:
            # spawnea el saler en la posicion de la nave
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def move(self, vel):
        pass

    def bullet_hell(self):
        """
        Esto recibe una input aleatoria y un gran contador
        """
        if self.bullet_hell_cool_down_counter == 0:
            for i in range(self.dificultad):
                laser = Laser(self.x-20, self.y, self.laser_img)
                self.lasers.append(laser)
