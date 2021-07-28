import pygame as pg
import random as rn
from personal.text import Text

class Card:
    def __init__(self, number, suit, pos):
        self.x, self.y = pos
        self.w, self.h = (75, 100)
        self.rect = pg.Rect((self.x, self.y, self.w, self.h))
        self.surf = pg.Surface((self.w, self.h))
        self.selected = False
        self.back = True

        if suit == 'cuori' or suit == 'quadri':
            color = (255, 0, 0)
        elif suit == 'fiori' or suit == 'picche':
            color = (0, 0, 0)
    
        self.number = Text(number, size=20, color=color)
        self.suit = suit

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    self.selected = not self.selected

    def render(self, screen):
        self.surf.fill(tuple(map(lambda x: x*int(not self.selected), (255, 255, 255))))
        pg.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.w, self.h), 5)
        screen.blit(self.surf, self.rect)
        self.number.render(screen, False, self.x+5, self.y+3)
        self.number.render(screen, False, self.x-10+self.w-5, self.y-20+self.h-5)
        
        if self.suit == 'quadri' or self.suit == 'fiori':
            d, D = 10, 20
            p1 = (self.x + int(self.w/2) - int(d/2), self.y + int(self.h/2))
            p2 = (p1[0] + d, p1[1])
            p3 = (self.x + int(self.w/2), self.y + int(self.h/2) - int(D/2))
            p4 = (p3[0], p3[1] + D)
            pg.draw.polygon(screen, (255*int(self.suit=='quadri'), 0, 0), [p1, p3, p2, p4])
        elif self.suit == 'cuori' or self.suit == 'picche':
            pg.draw.circle(screen, (255*int(self.suit=='cuori'), 0, 0),
                           (self.x + int(self.w/2), self.y + int(self.h/2)), 10)
        elif self.back:
            pg.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.w, self.h))


class Mazzo:
    def __init__(self):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['quadri', 'cuori', 'fiori', 'picche'] * 2
        Mazzo.cards = [Card(number, suit, (300, 400)) for number in numbers for suit in suits]
        rn.shuffle(Mazzo.cards)
        assert len(Mazzo.cards) == 104
        self.positions = [(int(800/2) - ((90*8-15)/2) + x*90, 150)
                              for x in range(8)]
