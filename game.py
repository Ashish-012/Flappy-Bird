import pygame
import sys
import random
pygame.init()


def draw_floor(floor_x): 
    window.blit(base,(floor_x,height-100))
    window.blit(base,(550+floor_x,height-100))
    if floor_x <= -550:
       return 0
    return floor_x

def create_pipe():
    pipe_rect = pipe_surface.get_rect(midtop = (500,400))
    return pipe_rect

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
        if pipe.centerx < -20:
            pipes.remove(pipe)
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        window.blit(pipe_surface,pipe)

# Screen Resolution
width = 550
height = 650

# setting caption and resolution
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flappy Bird")

# Game FPS
FPS = 120
clock = pygame.time.Clock()

# All images
background = pygame.image.load('assets/background-day.png')
background = pygame.transform.scale(background,(width,height))

base = pygame.image.load('assets/base.png')
base = pygame.transform.scale(base,(width,100))

bird = pygame.image.load('assets/bluebird-midflap.png')
bird = pygame.transform.scale(bird,(45,35))
bird_rect = bird.get_rect(center = (100,height//2))

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale(pipe_surface,(90,200))

pipes = []
pipe_height = []
spawn_pipe = pygame.USEREVENT
pygame.time.set_timer(spawn_pipe,1200)

floor_x = 0
gravity = 0.25
bird_movement = 0

play = True

while play:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
        if event.type == spawn_pipe:
            pipes.append(create_pipe())
            print(pipes)
            
                
    #drawing the background

    window.blit(background,(0,0))  

    #drawing the pipes
    pipes = move_pipes(pipes)
    draw_pipes(pipes)

    #drawing the floor
    
    floor_x -= 1
    floor_x = draw_floor(floor_x)

    #drawing the bird

    bird_movement += gravity
    bird_rect.centery += bird_movement
    window.blit(bird,bird_rect)

    

    #updating game window
    pygame.display.update()
    clock.tick(FPS)

