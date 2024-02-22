import pygame
from world import make_the_world, grass_tile, grass_tile2, flower_tile, tree_tile

# Pygame Setup
pygame.init()
pygame.display.set_caption('LLM Sprite')
clock = pygame.time.Clock()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
tile_size = 16  # Example size
animation_cooldown = 150  # Milliseconds between frame changes
last_animation_update = 0 

world_map = make_the_world(600, 600, 16)

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
            if tile_type['tile'] == "grass":
                screen.blit(grass_tile, (col * tile_size, row * tile_size))
            elif tile_type['tile'] == "grass2":
                screen.blit(grass_tile2, (col * tile_size, row * tile_size))
            elif tile_type['tile'] == "flowers":
                screen.blit(flower_tile, (col * tile_size, row * tile_size))            
            elif tile_type['tile'] == "tree":
                screen.blit(tree_tile, (col * tile_size, row * tile_size))
    # current_time = pygame.time.get_ticks()
    # if current_time - last_animation_update >= animation_cooldown:
    #     player["frame_index"] = (player["frame_index"] + 1) % len(player["images"][player["direction"]])
    #     last_animation_update = current_time

    # # Update which image to render
    # current_image = player["images"][player["direction"]][player["frame_index"]]
    # screen.blit(current_image, (player["x"] * tile_size, player["y"] * tile_size))

    pygame.display.update()

pygame.quit() 