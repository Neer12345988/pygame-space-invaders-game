import pygame
import os

pygame.font.init()
WIDTH = 900
HEIGHT = 500
CENTRE_X = 450
CENTRE_Y = 250

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space invaders")

BORDER = pygame.Rect(445, 0, 10, HEIGHT)
FPS = 60
VEL = 5
BUL_VEL = 7
MAX_BULS = 3
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

lives_font = pygame.font.SysFont("Comic Sans MS", 30)
winner_font = pygame.font.SysFont("Comic Sans MS", 100)

yellow_img = pygame.image.load("yellow.png")
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
red_img = pygame.image.load("red.png")
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
space_img = pygame.image.load("bg.png")
space = pygame.transform.scale(space_img, (WIDTH, HEIGHT))            