import pygame
import os
import time
import random
pygame.font.init()

# Imports para la pantalla y cargar las imagenes
from pantalla import WIDTH, HEIGHT, WIN
from loader import RED_SPACE_SHIP, GREEN_SPACE_SHIP, BLUE_SPACE_SHIP, YELLOW_SPACE_SHIP, RED_LASER, GREEN_LASER, BLUE_LASER, YELLOW_LASER, BG

# Logica Base
from Logica import collide
from Laser import Laser
from Ship import Ship
from Player import Player
from Enemy import Enemy




def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("helvetica", 50)
    lost_font = pygame.font.SysFont("helvetica", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 2.5

    player_vel = 6
    laser_vel = 6

    player = Player(WIDTH/2, HEIGHT/2)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        # ZONA DE RENDER ---------------------
        # Renderiza el Background
        WIN.blit(BG, (0,0))
        # Texto
        lives_label = main_font.render(f"Vidas: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255,255,255))
        # Texto de Vidas y Nivel
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        # Renderiza los enemigos
        for enemy in enemies:
            enemy.draw(WIN)
        # Renderiza el jugador
        player.draw(WIN)
        # END ZONA DE RENDER ------------------

        if lost:
            lost_label = lost_font.render("Changos!! Perdiste u.u", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        #if win: #en caso de ganar puedes agregar a un jefe
            # TODO
            # [] agregar un menu donde disparas a las partes del jefe que quieres
            # [] puedes escribir y guardar el nombre de este
            # [] agregar ese nivel como una funcion 

      #     pass

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        # Si se cumple cualquiera de estas condiciones el juego acaba
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

            # Entonces se ejecutara esto 
            # TODO
            # [] Confirmar que se pierde

            if lost:
                if lost_count > FPS * 3:
                    run = False
                else:
                    continue

        # Completa la Oleada
        if len(enemies) == 0:
            # TODO
            # [] Spawn un Jefe
            # [] agregarle un contador de jefes
                # leer de un archivo

            # Lee el archivo
            #with open(os.path.join(os.path.dirname( ), )):
            # aqui va una funcion especializada en seleccionar
            from Logica import leerSave
            pathRelativa = os.path.dirname(__file__)
            leerSave(pathRelativa)

            # tipo if level == -1 (entramos en la creacion de modos)

            level += 1
            wave_length += 3 

            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        if keys[pygame.K_ASTERISK]:
            print("Transportar a nivel de jefe")
            

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

def main_menu():
    title_font = pygame.font.SysFont("helvetica", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Espacio para entrar", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                main()
    pygame.quit()


main_menu()