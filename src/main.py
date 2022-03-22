import pygame

import sys


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, game, x, y, x_pos=0, y_pos=0, x_shift=0, y_shift=0,
            x_scale=1, y_scale=1, layer=0, groups=None, spritesheet=None):
        self._layer = layer
        groups = (game.all_sprites, ) if groups == None else (game.all_sprites, groups)
        super().__init__(groups)
        self.game = game

        x = x * Config.TILE_SIZE
        y = y * Config.TILE_SIZE
        self.width = Config.TILE_SIZE * x_scale
        self.height = Config.TILE_SIZE * y_scale

        self.x_pos = x_pos * Config.TILE_SIZE + x_shift
        self.y_pos = y_pos * Config.TILE_SIZE + y_shift

        if spritesheet == None:
            self.image = pygame.Surface([self.width-2, self.height-2])
            self.image.fill(Config.GREY)
        else:
            self.spritesheet = spritesheet
            self.image = self.spritesheet.get_sprite(
                self.x_pos,
                self.y_pos,
                self.width,
                self.height
            )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class CardSprite(BaseSprite):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, groups=game.ground, layer=0)
        #self.image.fill(Config.GREEN)

    #def update(self,event_list):


class Config:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GREY = (128, 128, 128)
    FPS = 30
    TILE_SIZE = 100
    MAX_GRAVITY = -3


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 30)
        self.screen = pygame.display.set_mode( (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT) ) 
        self.clock = pygame.time.Clock()

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.ground = pygame.sprite.LayeredUpdates()
        self.players = pygame.sprite.LayeredUpdates()

        # self.player = PlayerSprite(self, 10, 10)
        for i in range(9):
            for j in range(7):
                CardSprite(self, i, j)


    def handle_events(self,event_list):
        for event in event_list:
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("bruh")

    def update(self,event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("Doh")
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(Config.BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def game_loop(self):
        while self.playing:
            event_list = pygame.event.get()
            self.handle_events(event_list)
            self.update(event_list)
            self.draw()
            self.clock.tick(Config.FPS)

    
def main():
    g = Game()
    g.new()

    g.game_loop()

    pygame.quit()
    sys.exit()

