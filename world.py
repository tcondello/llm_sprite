
import pygame
import random

# Tile Structures
screen_width = 600
screen_height = 600

tile_definitions = [
    {"name": "grass", "biomes": ["forest", "flower_meadow"], "generation_probability": 0.8},
    {"name": "grass2", "biomes": ["flower_meadow"], "generation_probability": 0.2},
    {"name": "flowers", "biomes": ["flower_meadow"], "generation_probability": 0.4},
    {"name": "tree", "biomes": ["forest"], "generation_probability": 0.3}, 
    {"name": "water", "biomes": ["ocean"], "generation_probability": 0.2},  
    # ... more tile definitions ... 
]

tileset_image = pygame.image.load("tiles/basictiles.png")

def extract_tile(tileset, x, y, tile_size=16):
    rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
    tile_image = tileset.subsurface(rect)
    return tile_image

grass_tile = extract_tile(tileset_image, 0, 8)  
grass_tile2 = extract_tile(tileset_image, 1, 8) 
flower_tile = extract_tile(tileset_image, 4, 1)
water_tile = extract_tile(tileset_image, 5, 2) 
tree_tile = extract_tile(tileset_image, 6, 4)

import noise
import numpy as np  # Useful for array operations

def generate_heightmap(width, height, scale=10.0, octaves=6, persistence=0.5, lacunarity=2.0):
    world_map = np.zeros((height, width))  # Initialize empty map

    for y in range(height):
        for x in range(width):
            frequency = 1 
            amplitude = 1
            max_value = 0
            for octave in range(octaves):
                nx = x / scale * frequency 
                ny = y / scale * frequency 
                value = noise.pnoise2(nx, ny, octaves=1)  
                world_map[y][x] += value * amplitude

                amplitude *= persistence 
                frequency *= lacunarity

            max_value = max(max_value, world_map[y][x])
        
    world_map /= max_value  # Normalize values between 0 and 1

    return world_map

def map_height_to_tiles(width, height):
    heightmap = generate_heightmap(width, height, scale=10.0, octaves=6, persistence=0.5, lacunarity=2.0)
    # Modify thresholds to create the desired distribution of tiles
    grass_threshold = 0.35   
    flower_threshold = 0.75

    tile_map = []
    for row in heightmap:
        tile_row = []
        for height in row:
            if height < grass_threshold:
                tile_row.append({"tile": "grass", "biome": "grassland"}) 
            elif height < flower_threshold:
                tile_row.append({"tile": "grass2", "biome": "grassland"}) 
            else:
                tile_row.append({"tile": "flowers", "biome": "flower_meadow"}) 
        tile_map.append(tile_row)
    return tile_map
