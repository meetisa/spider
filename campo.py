import pygame as pg

from cards import Mazzo

class Distributor(Mazzo):
    def __init__(self):
        super().__init__()
        self.cards = Mazzo.cards[:40]

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pg.mouse.get_pos()):
            
        
        
class Piles(Mazzo):
    def __init__(self):
        super().__init__()
        self.cards = Mazzo.cards[40:]
        self.issues = 0

    def check(self, queue, index):
        previous = (self.)
        
    def update(self, event):
        if event

    def render(self, screen):
        for x, y in self.positions:
            
