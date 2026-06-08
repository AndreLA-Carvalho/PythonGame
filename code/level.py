#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys

import pygame  # type: ignore[import]

from code.const import C_CYAN, C_GREEN, C_WHITE, EVENT_ENEMY, MENU_OPTION, SPAWN_TIME, WIN_HEIGHT

from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000 # Tempo para completar o nível em milissegundos (20 segundos)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) # Define um timer para spawnar inimigos a cada SPAWN_TIME milissegundos (4 segundos)

        
    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3') # Carrega a música do nível
        pygame.mixer_music.play(-1) # Reproduz a música do nível em loop
        clock = pygame.time.Clock() # Cria um relógio para controlar o tempo do jogo
        while True:
            clock.tick(60) # Limita o jogo a 60 frames por segundo
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) # Desenha a entidade na janela
                ent.move() # Move a entidade
                if isinstance(ent, (Player, Enemy)): # Se a entidade for um jogador ou um inimigo, verifica se ele atirou
                    shoot = ent.shoot() # Verifica se o jogador atirou e retorna o tiro criado
                    if shoot is not None: # Se o jogador atirou, adiciona o tiro à lista de entidades do nível
                        self.entity_list.append(shoot) # Adiciona o tiro criado à lista de entidades do nível
                if ent.name == 'Player1':
                    self.level_text(text_size=14, text=f'Player1 - Health: {ent.health} | Score: {ent.score}', text_color=C_GREEN, text_pos=(10, 25)) # Exibe a saúde do Player1 na tela
                if ent.name == 'Player2':
                    self.level_text(text_size=14, text=f'Player2 - Health: {ent.health} | Score: {ent.score}', text_color=C_CYAN, text_pos=(10, 45)) # Exibe a saúde do Player2 na tela

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    sys.exit() # end pygame
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2')) # Escolhe aleatoriamente entre os dois tipos de inimigos
                    self.entity_list.append(EntityFactory.get_entity(choice)) # Adiciona o inimigo escolhido à lista de entidades do nível
                        
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color=C_WHITE, text_pos=(10, 5)) # Exibe o nome do nível e o tempo restante
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 35)) # Exibe o fps do jogo
            self.level_text(text_size=14, text=f'entidades:{len(self.entity_list)}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 20)) # Exibe o número de entidades na tela
            pygame.display.flip()  # Atualiza a janela
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list) # Verifica colisões entre as entidades
            EntityMediator.verify_health(entity_list=self.entity_list) # Verifica a saúde das entidades e remove as que tiverem saúde menor ou igual a 0
        pass
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size) # Cria a fonte do texto
        text_surf = Surface = text_font.render(text, True, text_color).convert_alpha() # Cria a superfície do texto
        text_rect = Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1]) # Cria o retângulo do texto
        self.window.blit(source=text_surf, dest=text_rect) # Desenha o texto na janela