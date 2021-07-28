import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((800, 600))

surf = pg.Surface((50, 50))
surf.fill((0, 255, 0))
rect = pg.Rect((400, 300, 50, 50))
moving = False

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            break
        
    pos = pg.mouse.get_pos()
    if pg.mouse.get_pressed()[0]:
        if rect.collidepoint(pos):
            moving = True
    else:
        moving = False

    if moving:
        print(f'muovendosi... {pos}')
        rect.center = pos
        
    screen.fill((255, 0, 0))
    screen.blit(surf, rect)
    pg.display.update()


pg.quit()
sys.exit()
