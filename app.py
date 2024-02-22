import pygame
import random

# Pygame Setup
pygame.init()
pygame.display.set_caption('LLM Sprite')
clock = pygame.time.Clock()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
tile_size = 16  # Example size

# Tile Structures
tile_types = ["grass", "grass2", "flowers", "trees"]
tile_size = 16  # Example size
tile_width = 16
tile_height = 16
tileset_image = pygame.image.load("tiles/basictiles.png").convert_alpha()
columns = screen_width // tile_size
rows = screen_height // tile_size

def extract_tile(tileset, x, y):
    rect = pygame.Rect(x * tile_width, y * tile_height, tile_width, tile_height)
    tile_image = tileset.subsurface(rect)
    return tile_image

grass_tile = extract_tile(tileset_image, 0, 8)  
grass_tile2 = extract_tile(tileset_image, 1, 8) 
flower_tile = extract_tile(tileset_image, 4, 1) 
tree_tile = extract_tile(tileset_image, 6, 4)  
## End Tile Structure

# Create the world map
world_map = []
for row in range(rows):
    map_row = []  # Create an empty row
    for col in range(columns):
        tile_type = random.choice(tile_types)
        map_row.append(tile_type)  
    world_map.append(map_row)  

# Sprite
sprite_image = pygame.image.load("sprite/characters.png").convert_alpha()
player_idle = extract_tile(sprite_image, 4,0)
player_right1 = extract_tile(sprite_image, 3,2)
player_right2 = extract_tile(sprite_image, 4,2)
player_right3 = extract_tile(sprite_image, 5,2)
player_left1 = extract_tile(sprite_image, 3,1)
player_left2 = extract_tile(sprite_image, 4,1)
player_left3 = extract_tile(sprite_image, 5,1)
player_up1 = extract_tile(sprite_image, 3,3)
player_up2 = extract_tile(sprite_image, 4,3)
player_up3 = extract_tile(sprite_image, 5,3)
player_down1 = extract_tile(sprite_image, 3,0)
player_down2 = extract_tile(sprite_image, 4,0)
player_down3 = extract_tile(sprite_image, 5,0)
# ... Load images for left, up, down directions ... 

player = {
    "x": 0,
    "y": 0,
    "direction": "idle",
    "images": {
        "idle": [player_idle, player_idle,player_idle],
        "right": [player_right1, player_right2, player_right3],
        "left": [player_left1, player_left2, player_left3],
        "up": [player_up1, player_up2, player_up3],
        "down": [player_down1, player_down2, player_down3]
        # ... similar for "up" and "right"
    },
    "frame_index": 0  # To track which frame of the animation we're on
}
animation_cooldown = 150  # Milliseconds between frame changes
last_animation_update = 0 

def player_movement_logic(player_dic):
    new_x = player_dic['x']
    new_y = player_dic['y']

    if event.key == pygame.K_LEFT:
        new_x -= 1
        direction = "left" 
    elif event.key == pygame.K_RIGHT:
        new_x += 1
        direction = "right" 
    elif event.key == pygame.K_UP:
        new_y -= 1
        direction = "up" 
    elif event.key == pygame.K_DOWN:
        new_y += 1
        direction = "down" 
    # Obstacle Collision Check    
    tile_at_target_x = world_map[new_y][new_x] 
    if tile_at_target_x not in ["trees", "rock"]:
        # Boundary Check
        if 0 <= new_x < columns and 0 <= new_y < rows:
            player_dic['x'] = new_x
            player_dic['y'] = new_y
            player_dic['direction'] = direction 

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                             
        if event.type == pygame.KEYDOWN:
            player_movement_logic(player)

    # Basic Rendering (adapt as needed)
    screen.fill((0, 0, 0))  # Black background
    for row in range(len(world_map)):
        for col in range(len(world_map[0])):
            tile_type = world_map[row][col]             
            if tile_type == "grass":
                screen.blit(grass_tile, (col * tile_size, row * tile_size))
            elif tile_type == "grass2":
                screen.blit(grass_tile2, (col * tile_size, row * tile_size))
            elif tile_type == "flowers":
                screen.blit(flower_tile, (col * tile_size, row * tile_size))            
            elif tile_type == "trees":
                screen.blit(tree_tile, (col * tile_size, row * tile_size))
    current_time = pygame.time.get_ticks()
    if current_time - last_animation_update >= animation_cooldown:
        player["frame_index"] = (player["frame_index"] + 1) % len(player["images"][player["direction"]])
        last_animation_update = current_time

    # Update which image to render
    current_image = player["images"][player["direction"]][player["frame_index"]]
    screen.blit(current_image, (player["x"] * tile_size, player["y"] * tile_size))

    pygame.display.update()

pygame.quit() 