#gui/board_view.py
import pygame

class BoardView:
    def __init__(self, deck):
        self.deck = deck

        self.card_width = 100
        self.card_height = 140
        self.spacing = 20

    def draw_cascades(self, screen, screen_width):
        total_cascades_width = (8 * self.card_width) + (7 * self.spacing)
        start_x = (screen_width - total_cascades_width) // 2
        start_y = 220

        for i in range(8):
            col_x = start_x + i * (self.card_width + self.spacing)
            if ('A', 'hearts') in self.deck:
                card_img = self.deck[('A', 'hearts')]
                card_rect = card_img.get_rect(topleft=(col_x, start_y))
                screen.blit(card_img, card_rect)

    def draw(self, screen, screen_width, screen_height):
        self.draw_cascades(screen, screen_width)