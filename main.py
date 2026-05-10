import pygame
import os

pygame.font.init()
pygame.mixer.init()
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
BULLET_HIT_SOUND = pygame.mixer.Sound("Grenade+1.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("Gun+Silencer.mp3")

lives_font = pygame.font.SysFont("Comic Sans MS", 30)
winner_font = pygame.font.SysFont("Comic Sans MS", 100)

yellow_img = pygame.image.load("yellow.png")
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
red_img = pygame.image.load("red.png")
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
space_img = pygame.image.load("bg.png")
space = pygame.transform.scale(space_img, (WIDTH, HEIGHT))    

def draw_window(red, yellow, red_bullets, yellow_bullets, red_lives, yellow_lives):
    screen.blit(space, (0,0))
    pygame.draw.rect(screen, "black", BORDER)

    red_text = lives_font.render(f"Lives: {red_lives}", 1, "white")
    screen.blit(red_text, (WIDTH - red_text.get_width() - 10, 10))

    yellow_text = lives_font.render(f"Lives: {yellow_lives}", 1, "white")
    screen.blit(yellow_text, (10, 10))

    screen.blit(red_spaceship, (red.x, red.y))
    screen.blit(yellow_spaceship, (yellow.x, yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(screen, "red", bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(screen, "yellow", bullet)

    pygame.display.update()

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL < HEIGHT - 15:
        red.y += VEL