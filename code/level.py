#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import pygame  # type: ignore[import]

from code.const import COLOR_WHITE, WIN_HEIGHT

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))
        self.timeout = 20000 # Tempo para completar o nível em milissegundos (20 segundos)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3') # Carrega a música do nível
        pygame.mixer_music.play(-1) # Reproduz a música do nível em loop
        clock = pygame.time.Clock() # Cria um relógio para controlar o tempo do jogo
        while True:
            clock.tick(60) # Limita o jogo a 60 frames por segundo
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    sys.exit() # end pygame
                    
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color=COLOR_WHITE, text_pos=(10, 5)) # Exibe o nome do nível e o tempo restante
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 35)) # Exibe o fps do jogo
            self.level_text(text_size=14, text=f'entidades:{len(self.entity_list)}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 20)) # Exibe o número de entidades na tela
            pygame.display.flip()  # Atualiza a janela
        pass
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size) # Cria a fonte do texto
        text_surf = Surface = text_font.render(text, True, text_color).convert_alpha() # Cria a superfície do texto
        text_rect = Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1]) # Cria o retângulo do texto
        self.window.blit(source=text_surf, dest=text_rect) # Desenha o texto na janela