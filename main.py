import pygame as pg
import sys

import cards


pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Spider')

carta = cards.Card('7', 'cuori', (300, 400))
mazzo = cards.Mazzo()
slot = [(int(800/2) - ((90*8-15)/2) + x*90, 30) for x in range(8)]
clock = pg.time.Clock()
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            break
        mazzo.update(event)

        
    screen.fill((139, 74, 237))
    for x, y in slot:
        pg.draw.rect(screen, (237, 138, 66), (x, y, 75, 100), border_radius=5)
        
    mazzo.render(screen)
    pg.display.update()
    clock.tick(30)

pg.quit()
sys.exit()
