
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

def get_adjacent_tiles(world_map, row, col):
    if len(world_map) == 0:  # Temporary check for empty map
        return [{"tile": "grass", "biome": None}] * 8 # Placeholder neighbors
    
    adjacent_tiles = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            adj_row = (row + dy) % len(world_map)
            adj_col = (col + dx) % len(world_map[0]) 
            adjacent_tiles.append(world_map[adj_row][adj_col])
    return adjacent_tiles

def apply_cellular_automata(world_map):
    new_map = []
    for row in range(len(world_map)):
        new_row = []
        for col in range(len(world_map[0])):
            neighbors = get_adjacent_tiles(world_map, row, col)
            num_tree_neighbors = sum(tile["tile"] == "tree" for tile in neighbors)

            current_tile = world_map[row][col]
            if current_tile["tile"] == "flowers":
                new_tile = "tree" if num_tree_neighbors >= 3 else random.choice(["grass2", "flowers"])

            new_row.append({"tile": new_tile, "biome": "forest"})  # Adjust if needed 
        new_map.append(new_row)
    return new_map

# Create the world map
def make_the_world(screen_width, screen_height, tile_size, forest_density=0.1, clustering_bonus=0.09):
    columns = screen_width // tile_size
    rows = screen_height // tile_size
    world_map = []
    for row in range(rows):
        map_row = []  
        for col in range(columns):
            tree_probability = forest_density
            neighbors = get_adjacent_tiles(world_map, row, col)
            for tile in neighbors:
                if tile["tile"] in ["grass", "grass2"] and random.random() < 0.3:  # Example probability 
                    tile["tile"] = "flowers"
                    tile["biome"] = "flower_meadow"
            num_tree_neighbors = sum(tile["tile"] == "tree" for tile in neighbors)
            tree_probability += clustering_bonus * num_tree_neighbors 

            tree_probability = min(1.0, tree_probability)  # Keep it within 0-1 range

            if random.random() < tree_probability:
                tile_data = {"tile": "tree", "biome": "forest"}
            else:
                tile_data = {"tile": "grass", "biome": None} 
            map_row.append(tile_data)
        world_map.append(map_row) 
        # print(world_map)
    world_map2 = apply_cellular_automata(world_map)  # Apply the CA step     
    return world_map2


