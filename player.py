import pygame as pg
import colors as cls
import settings as sets

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(cls.dark_cyan)
        self.rect = self.image.get_rect()
        self.rect.center =(sets.WIDTH/2,sets.HEIGHT/2)

    def up_and_down(self):

        self.rect.bottom+=2
        if self.rect.top < sets.HEIGHT:
            self.rect.bottom-=2
        if self.rect.bottom > sets.HEIGHT:
            self.rect.top +=2


    def update(self):
        self.up_and_down()
        self.rect.x +=5
        if self.rect.left > sets.WIDTH:
            self.rect.right =0
    


