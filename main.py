import pygame as pg
import random as rnd
import player as py
import settings as sets
import colors as cls

pg.init()
screen = pg.display.set_mode((sets.WIDTH, sets.HEIGHT))
pg.display.set_caption(' My new game ')
clock = pg.time.Clock()

all_groups = pg.sprite.Group()
player1 = py.Player()
all_groups.add(player1)



running = True
while running:
    clock.tick(sets.FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 

    screen.fill(cls.indian_red)
    all_groups.draw(screen)
    all_groups.update()
    pg.display.flip()
pg.quit()


