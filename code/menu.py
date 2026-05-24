#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import Font, Rect, Surface
import pygame.image

from code.const import COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, WIN_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menuBg.png') # Carrega a imagem do menu
        self.rect = self.surf.get_rect(left=0, top=0) # cria o retângulo da imagem do menu

    def run(self, ):
        pygame.mixer_music.load('./asset/menu.mp3') # Carrega a música do menu
        pygame.mixer_music.play(-1) # Reproduz a música do menu em loop
        
        while True:
            self.window.blit(source=self.surf, dest=self.rect) # Desenha a imagem do menu na janela
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            
            pygame.display.flip() # Atualiza a janela
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    quit() # end pygame
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size) # Cria a fonte do texto
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() # Cria a superfície do texto
        text_rect: Rect = text_surf.get_rect(center=text_center_pos) # Cria o retângulo do texto
        self.window.blit(source=text_surf, dest=text_rect) # Desenha o texto na janela
