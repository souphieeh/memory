import pygame

pygame.init()

# Variables for Game
gameWidth = 840
gameHeight = 640

# Loading the pygame screen
screen = pygame.display.set_mode((gameWidth, gameHeight))

gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

pygame.quit()