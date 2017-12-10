from math import sin, cos
from array import array
from struct import unpack

import pygame

screen_x = 512
screen_y = 512

screen_fov = 90 #degree

voxel_size = 256 #pixels
voxel_real = 0.0512 #meters

def ray(x, y):


def voxel(x, y, z):


'init pygame display'
pygame.display.init()
pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Test','Test')

surface = pygame.display.get_surface()
surface.fill((0, 255, 0))

pygame.display.flip()

input("Press Enter to continue...")
