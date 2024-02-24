import pygame

class Tile(object):
    def __init__(self, name, biomes, generation_height, x, y, tile_size, tile_set_image):
            self.name = name 
            self.biomes = biomes 
            self.generation_height = generation_height            
            tile_size = tile_size
            tile_set_image = pygame.image.load(tile_set_image)            
            x = x 
            y = y 
            rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            self.tile_image = tile_set_image.subsurface(rect)

    def to_dict(self):    
          return {k: v for k,v in sorted(vars(self).items())}

   