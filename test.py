
import pygame
import random
import noise
import numpy as np
from tile_class import Tile

class WorldTiles(object):
    def __init__(self, screen_width=600, screen_height=600, tile_size=16, tile_set_image="tiles/basictiles.png"):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tile_size = tile_size
        self.tile_set_image = tile_set_image                        
        self.heightMap = np.zeros((self.screen_height, self.screen_width))
        self.grass_tile = Tile(
            name="grass", 
             biomes=["forest", "flower_meadow"], 
             generation_height=0.2, 
             x=0, 
             y=8,
             tile_size=self.tile_size,
             tile_set_image=self.tile_set_image            
        ).to_dict()
        self.grass2_tile = Tile(
            name="grass2", 
             biomes=["flower_meadow"], 
             generation_height=0.3, 
             x=1, 
             y=8,
             tile_size=self.tile_size,
             tile_set_image=self.tile_set_image            
        ).to_dict()
        self.flower_tile = Tile(
            name="flower", 
             biomes=["flower_meadow"], 
             generation_height=0.4, 
             x=4, 
             y=1,
             tile_size=self.tile_size,
             tile_set_image=self.tile_set_image            
        ).to_dict()
        self.tree_tile = Tile(
            name="tree", 
             biomes=["forest"], 
             generation_height=0.5, 
             x=6, 
             y=4,
             tile_size=self.tile_size,
             tile_set_image=self.tile_set_image            
        ).to_dict()
        self.water_tile = Tile(
            name="water", 
             biomes=["pond"], 
             generation_height=0.1, 
             x=5, 
             y=2,
             tile_size=self.tile_size,
             tile_set_image=self.tile_set_image            
        ).to_dict()
        self.tile_definitions = []

class GenerateHeightmap(WorldTiles):
    def __init__(self, scale=10, octaves=6, persistence=0.5, lacunarity=2, frequency=1, amplitude=1, max_value=0):
        super(GenerateHeightmap, self).__init__()
        self.scale = scale 
        self.octaves = octaves 
        self.persistence = persistence 
        self.lacunarity = lacunarity
        
        for y in range(self.screen_height):
            for x in range(self.screen_width):
                frequency = 1 
                amplitude = 1
                max_value = 0
                for octave in range(self.octaves):
                    nx = x / self.scale * frequency 
                    ny = y / self.scale * frequency 
                    value = noise.pnoise2(nx, ny, octaves=1)  # I dont understand what this line is doing
                    self.heightMap[y][x] += value * amplitude
                    amplitude *= self.persistence 
                    frequency *= self.lacunarity
                max_value = max(max_value, self.heightMap[y][x])            
        self.heightMap /= max_value  # Normalize values between 0 and 1
     

class MakeTheWorld(GenerateHeightmap):
    def __init__(self):
        super(MakeTheWorld, self).__init__()
        self.tile_map = []
        for row in self.heightMap:
            tile_row = []
            for height in row:
                # figure out how to do this checking across all generation probability and append it to a new list more efficiently
                if height <= self.water_tile.get('generation_height'):
                    tile_row.append(self.water_tile)
                elif height < self.grass_tile.get('generation_height'):
                    tile_row.append(self.grass_tile)
                elif height < self.grass2_tile.get('generation_height'):
                    tile_row.append(self.grass2_tile)      
                elif height < self.flower_tile.get('generation_height'):
                    tile_row.append(self.flower_tile)
                elif height < self.tree_tile.get('generation_height'):
                    tile_row.append(self.tree_tile)                     
                else:
                    tile_row.append(self.tree_tile) 
            self.tile_map.append(tile_row)        

world_map = MakeTheWorld().tile_map
print(world_map)