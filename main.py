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
from Jefe import Jefe

def spawn(enemies, wave_length):
    # Spawn de Enemigos
    for i in range(wave_length):
        enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
        enemies.append(enemy)

def spawn_jefe():
    # Jefe(x,y, tipo, parte)
    # props externas temporalmente puestas aqui
    tipo = "HORROR"

    pSY = HEIGHT/8 #puntoSpawnY
    pSX = WIDTH/2  #puntoSpawnX
    # Spawnea 4 objetos del Jefe
    brazo_derecho = Jefe(pSX + 30, pSY + 20, tipo, parte="right")
    brazo_izquierdo = Jefe(pSX + 30, pSY + 20, tipo, parte="left")
    ojo = Jefe(pSX, pSY + 40, tipo, parte="eye")
    cabeza = Jefe(pSX, pSY, tipo, parte="head")

    print("Aqui se imprime un jefecito, por implementar :p")
    return ojo, cabeza, brazo_izquierdo, brazo_derecho


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
    laser_vel = 8
    # spawn de player
    player = Player(WIDTH/2, HEIGHT/2)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # Counter para Jefe
    # cada nivel se reduce y se llega a 0
    # 1 significa que habra un nivel normal y entonces un jefe
    # 2 signifca dos niveles normales y entonces un jefe
    counter_jefe = 1

    def redraw_window():
        # ZONA DE RENDER ---------------------
        # Renderiza el Background
        WIN.blit(BG, (0,0))
        # Texto
        lives_label = main_font.render(f"Vidas: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255,255,255))
        # Texto de Vidas y Nivel
        WIN.blit(lives_label, (10, 50))
        WIN.blit(level_label, (10, 10))
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

        # ------------------- ZONA DE CAMBIO DE NIVEL ---------------------
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

            # subir la dificultad
            level, wave_length = level + 1, wave_length + 2

            # Aparece un jefe en el nivel 2, 5, 7, ...
            if counter_jefe == 0:
                enemis = spawn_jefe()
                counter_jefe += 2
            else:
                # Spawn de los enemigos
                spawn(enemies, wave_length)
                counter_jefe -= 1

        # ------------------- END ZONA DE CAMBIO DE NIVEL ---------------------

        # ------------------ ZONA DE CONTROLES -------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if ( keys[pygame.K_a] or keys[ pygame.K_LEFT ]) and player.x - player_vel > 0: # left
            player.x -= player_vel
        if ( keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if ( keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player_vel > 0: # up
            player.y -= player_vel
        if ( keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        if keys[pygame.K_k]:
            print("Transportar a nivel de jefe")
            enemies = spawn_jefe()

        # salir del juego con Escape 
        if keys[pygame.K_ESCAPE]:
            quit()
            
        # ------------------ END ZONA DE CONTROLES -------------------------------


        # Logica de Enemigos
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

        #Los lasers del jugador van hacia arriba
        player.move_lasers(-laser_vel, enemies)

def main_menu():
    title_font = pygame.font.SysFont("helvetica", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label0 = title_font.render("Science and Commit", 1, (255,255,255))
        title_label = title_font.render("Espacio para entrar", 1, (255,255,255))
        WIN.blit(title_label0, (WIDTH/2 - title_label.get_width()/2, 100))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                main()
    pygame.quit()


main_menu()