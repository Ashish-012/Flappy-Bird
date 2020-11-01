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
    random_height = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (600,random_height))
    top_pipe = pipe_surface.get_rect(midbottom = (600,random_height-220))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
        if pipe.centerx < -20:
            pipes.remove(pipe)
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >=650 :
            window.blit(pipe_surface,pipe)
        
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            window.blit(flip_pipe,pipe)


def check_collisions(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= height-100:
        return False

    return True

def render_score():
    score_display = score_font.render(str(int(score)), True, (255,255,255) )
    score_rect = score_display.get_rect(center = (width//2, 120))
    window.blit(score_display, score_rect)

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
pipe_surface = pygame.transform.scale(pipe_surface,(90,600))

pipes = []
pipe_height = [260,300,340,360,380,400,420,460,480,500,510]


game_over_image = pygame.image.load('assets/gameover.png')
game_over_image = pygame.transform.scale(game_over_image,(380,100))
game_over_rect = game_over_image.get_rect(center = (width//2,height//2))

score_font = pygame.font.Font('04B_19.ttf',40)


spawn_pipe = pygame.USEREVENT
pygame.time.set_timer(spawn_pipe,1200)

floor_x = 0
gravity = 0.25
bird_movement = 0
score = 0

play = True
game_active = True

while play:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == True:
                bird_movement = 0
                bird_movement -= 8
                
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                bird_rect.center = (100,height//2)
                pipes.clear()
                bird_movement= 0
                score = 0
                
        if event.type == spawn_pipe and game_active == True:
            pipes.extend(create_pipe())
            
                
    #drawing the background

    window.blit(background,(0,0))  

    if game_active == True:
        #drawing the pipes
        pipes = move_pipes(pipes)
        draw_pipes(pipes)
        
        #drawing the bird

        bird_movement += gravity
        bird_rect.centery += bird_movement
        window.blit(bird,bird_rect)

        #drawing the score

        render_score()
        score += 0.01

        # collisions

        game_active = check_collisions(pipes)

    
    else:
        window.blit(game_over_image, game_over_rect)

    #drawing the floor
    
    floor_x -= 4
    floor_x = draw_floor(floor_x)
    
    #updating game window
    pygame.display.update()
    clock.tick(FPS)

