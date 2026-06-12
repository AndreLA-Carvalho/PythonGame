#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import Font, Rect, Surface
import pygame.image

from code.const import C_ORANGE, C_WHITE, C_YELLOW, MENU_OPTION, WIN_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menuBg.png').convert_alpha() # Carrega a imagem do menu
        self.rect = self.surf.get_rect(left=0, top=0) # cria o retângulo da imagem do menu

    def run(self):
        menu_option = 0 # Opção do menu selecionada, começa na primeira opção
        pygame.mixer_music.load('./asset/menu.mp3') # Carrega a música do menu
        pygame.mixer_music.play(-1) # Reproduz a música do menu em loop
        
        while True:
            # Draw images
            self.window.blit(source=self.surf, dest=self.rect) # Desenha a imagem do menu na janela
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip() # Atualiza a janela
            
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    quit() # end pygame
                if event.type == pygame.KEYDOWN: # Check for key press
                    if event.key == pygame.K_DOWN: # Check for down arrow key
                        if menu_option < len(MENU_OPTION) - 1: # Check if the menu option is less than the last option
                            menu_option += 1 # Move down the menu option
                        else:
                            menu_option = 0 # Move to the first option
                    if event.key == pygame.K_UP: # Check for up arrow key
                        if menu_option > 0: # Check if the menu option is greater than the first option
                            menu_option -= 1 
                        else:
                            menu_option = len(MENU_OPTION) - 1 # Move to the last option
                    if event.key == pygame.K_RETURN: # Check for enter key
                        return MENU_OPTION[menu_option] # Return the selected menu option
        
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size) # Cria a fonte do texto
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() # Cria a superfície do texto
        text_rect: Rect = text_surf.get_rect(center=text_center_pos) # Cria o retângulo do texto
        self.window.blit(source=text_surf, dest=text_rect) # Desenha o texto na janela
