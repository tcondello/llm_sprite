import pygame
from world import MakeTheWorld

# Pygame Setup
pygame.init()
pygame.display.set_caption('LLM Sprite')
clock = pygame.time.Clock()
screen_width = 900
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
tile_size = 16  # Example size
tile_set_image="tiles/basictiles.png"
animation_cooldown = 150  # Milliseconds between frame changes
last_animation_update = 0 

world_map = MakeTheWorld(screen_height, screen_width, tile_size, tile_set_image, scale=10, octaves=6, persistence=0.5, lacunarity=2, frequency=1, amplitude=1, max_value=0).tile_map

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                             
        # if event.type == pygame.KEYDOWN:
            # player_movement_logic(player)

    # Basic Rendering (adapt as needed)
    screen.fill((0, 0, 0))  # Black background
    for row in range(len(world_map)):
        for col in range(len(world_map[0])):
            tile_type = world_map[row][col]             
            if tile_type.get('name') == "water":
                screen.blit(tile_type.get('tile_image'), (col * tile_size, row * tile_size))
            elif tile_type.get('name') == "grass":
                screen.blit(tile_type.get('tile_image'), (col * tile_size, row * tile_size))
            elif tile_type.get('name') == "grass2":
                screen.blit(tile_type.get('tile_image'), (col * tile_size, row * tile_size))
            elif tile_type.get('name') == "flower":
                screen.blit(tile_type.get('tile_image'), (col * tile_size, row * tile_size))
            elif tile_type.get('name') == "tree":
                screen.blit(tile_type.get('tile_image'), (col * tile_size, row * tile_size))
    # current_time = pygame.time.get_ticks()
    # if current_time - last_animation_update >= animation_cooldown:
    #     player["frame_index"] = (player["frame_index"] + 1) % len(player["images"][player["direction"]])
    #     last_animation_update = current_time

    # # Update which image to render
    # current_image = player["images"][player["direction"]][player["frame_index"]]
    # screen.blit(current_image, (player["x"] * tile_size, player["y"] * tile_size))

    pygame.display.update()

pygame.quit() 