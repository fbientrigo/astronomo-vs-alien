from pygame import image, transform
import os
from pantalla import WIDTH, HEIGHT

# Load images
RED_SPACE_SHIP = image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = image.load(os.path.join("assets", "pixel_laser_yellow.png"))


# Background
BG = transform.scale(image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
