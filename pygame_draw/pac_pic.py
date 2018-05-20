import pygame
import pygame.gfxdraw
from math import radians

pygame.init()
#colors in RGB
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
yellow = (255, 255,0)

# Create a sized black screen
height = 1000
width = 200
screen = pygame.display.set_mode([height, width])
screen.fill(black)

# Set the title and icon of the window
pygame.display.set_caption('Pacman')
icon = pygame.image.load('inky.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
start_angle = 35
end_angle = 325
status = "open"
x = 100
wave = 13

def draw_ghost():
    pygame.draw.line(screen, blue, (700, 145), (700, 80), 1)
    pygame.draw.line(screen, blue, (800, 145), (800, 80), 1)
    pygame.draw.arc(screen, blue, [700, 50, 100, 70], 0, radians(180), 1)
    pygame.draw.circle(screen, white, (725,92), 12, 0)
    pygame.draw.circle(screen, blue, (720,92), 6, 0)
    pygame.draw.circle(screen, white, (765,92), 12, 0)
    pygame.draw.circle(screen, blue, (760,92), 6, 0)
    global wave
    pygame.draw.arc(screen, blue, [700, 145, 20, wave], 0, radians(180), 1)
    pygame.draw.arc(screen, blue, [720, 145, 20, wave], radians(180), 0 , 1)
    pygame.draw.arc(screen, blue, [740, 145, 20, wave], 0, radians(180), 1)
    pygame.draw.arc(screen, blue, [760, 145, 20, wave], radians(180), 0, 1)
    pygame.draw.arc(screen, blue, [780, 145, 20, wave], 0, radians(180),  1)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    #pygame.draw.circle(screen, yellow, (100, 100), 60)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if x != 1070:
                x += 4
            if status == "open":
                if start_angle == 2:
                    status = "close"
                else:
                    wave -= 1
                    start_angle -= 3
                    end_angle += 3
            if status == "close":
                if start_angle == 35:
                    status = "open"
                else:
                    wave += 1
                    start_angle += 3
                    end_angle -= 3
    screen.fill(black)
    pygame.gfxdraw.pie(screen, x, 100, 60, start_angle, end_angle, yellow)
    if x < 750:
        draw_ghost()
    pygame.display.update() 
    clock.tick(60)

# elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 self.moving_left = False
#             elif event.key == pygame.K_RIGHT:
#                 self.moving_right = False