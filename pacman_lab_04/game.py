import pygame

pygame.init()
#colors in RGB
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
purple = (255,0,255)
yellow = (255, 255,0)

# Create a sized black screen
height = 500
width = 500
screen = pygame.display.set_mode([height, width])
screen.fill(black)

# Set the title and icon of the window
pygame.display.set_caption('Pacman')
icon = pygame.image.load('any.png')
pygame.display.set_icon(icon)

#walls
def walls():
    pygame.draw.lines(screen, blue, True, [(5,5), (width-5,5), (width-5,height-5), (5,height-5)], 5)
    pygame.draw.lines(screen, blue, False, [(220, 200), (180,200), (180,300), (320, 300), (320, 200), (280, 200)], 5)
    pygame.draw.lines(screen, white, False, [(220, 200), (280,200)], 3)

    block1 = [(50, 200), (50,50), (200,50), (200, 100), (80, 100), (80, 200)]
    pygame.draw.lines(screen, blue, True, block1, 5)

    block2 = [(50, 300), (50, 445), (200,445), (200, 400), (80, 400), (80, 300)]
    pygame.draw.lines(screen, blue, True, block2, 5)

    block3 = [(295, 445), (445, 445), (445,295), (420, 295), (420, 395), (295, 395)]
    pygame.draw.lines(screen, blue, True, block3, 5)

    block4 = [(295, 50), (445, 50), (445,200), (420, 200), (420, 100), (295, 100)]
    pygame.draw.lines(screen, blue, True, block4, 5)


    
    pygame.draw.lines(screen, blue, False, [(250, 5), (250, 60)], 5)
    pygame.draw.lines(screen, blue, False, [(5, 250), (45, 250)], 5)
    pygame.draw.lines(screen, blue, False, [(250, 495), (250, 440)], 5)
    pygame.draw.lines(screen, blue, False, [(495, 250), (450, 250)], 5)

    pygame.draw.lines(screen, blue, False, [(250, 110), (250, 150)], 5)
    pygame.draw.lines(screen, blue, False, [(180, 150), (320, 150)], 5)

    pygame.draw.lines(screen, blue, False, [(95, 250), (130, 250)], 5)
    pygame.draw.lines(screen, blue, False, [(130, 150), (130, 350)], 5)

    pygame.draw.lines(screen, blue, False, [(250, 395), (250, 350)], 5)
    pygame.draw.lines(screen, blue, False, [(180, 350), (320, 350)], 5)

    pygame.draw.lines(screen, blue, False, [(405, 250), (370, 250)], 5)
    pygame.draw.lines(screen, blue, False, [(370, 150), (370, 350)], 5)

class Ghost:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
    def show(self, screen):
        screen.blit(self.image, [self.x, self.y])

ghost = Ghost(205, 215, "ghost1.png")

class Pacman:
    def __init__(self, dx, dy, filename):
        self.imagename = filename
        self.image = pygame.image.load(self.imagename)

        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self.image = pygame.image.load(self.imagename)
        if self.moving_left:
            if self.rect.x > 10:
                self.rect.x -= 4
        if self.moving_right:
            if self.rect.x < width-40:
                self.rect.x += 4
        if self.moving_up:
            if self.rect.y > 10:
                self.rect.y -= 4
        if self.moving_down:
            if self.rect.y < height-40:
                self.rect.y += 4

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.moving_left = True
                self.imagename = "pacmanleft.png"
            elif event.key == pygame.K_RIGHT:
                self.moving_right = True
                self.imagename = "pacmanright.png"
            elif event.key == pygame.K_UP:
                self.moving_up = True
                self.imagename = "pacmanup.png"
            elif event.key == pygame.K_DOWN:
                self.moving_down = True
                self.imagename = "pacmandown.png"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.moving_right = False
            elif event.key == pygame.K_UP:
                self.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.moving_down = False

    def show(self, screen):
        screen.blit(self.image, self.rect)

pacman = Pacman(50, 50, "pacmanright.png")
clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        pacman.handle_event(event)
    pacman.update()
    screen.fill(black)
    walls()
    pacman.show(screen)
    ghost.show(screen)
    pygame.display.update() 
    clock.tick(60)

#show until the user quits
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
