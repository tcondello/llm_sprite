import pygame 

def extract_tile(tileset, x, y, tile_size=16):
    rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
    tile_image = tileset.subsurface(rect)
    return tile_image

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
