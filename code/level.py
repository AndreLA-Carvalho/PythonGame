#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys

import pygame  # type: ignore[import]

from code.const import C_CYAN, C_GREEN, C_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, MENU_OPTION, SPAWN_TIME, TIMEOUT_LEVEL, TIMEOUT_STEP, WIN_HEIGHT

from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window: pygame.Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player_score = player_score
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(f"{self.name.lower()}bg"))
        player = EntityFactory.get_entity('Player1')
        player.score = self.player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = self.player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) # Define um timer para spawnar inimigos a cada SPAWN_TIME milissegundos (4 segundos)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) 
        
    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3') # Carrega a música do nível
        pygame.mixer_music.play(-1) # Reproduz a música do nível em loop
        pygame.mixer_music.set_volume(0.3)
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
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP # Diminui o tempo restante para completar o nível
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                self.player_score[0] = ent.score # Atualiza a pontuação do Player1
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                self.player_score[1] = ent.score # Atualiza a pontuação do Player2
                        return True # Retorna True para indicar que o nível foi completado com sucesso
                    
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                        break
                if not found_player:
                    return False # Retorna False para indicar que o nível foi perdido
                        
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color=C_WHITE, text_pos=(10, 5)) # Exibe o nome do nível e o tempo restante
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 35)) # Exibe o fps do jogo
            self.level_text(text_size=14, text=f'entidades:{len(self.entity_list)}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 20)) # Exibe o número de entidades na tela
            pygame.display.flip()  # Atualiza a janela
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list) # Verifica colisões entre as entidades
            EntityMediator.verify_health(entity_list=self.entity_list) # Verifica a saúde das entidades e remove as que tiverem saúde menor ou igual a 0
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size) # Cria a fonte do texto
        text_surf = Surface = text_font.render(text, True, text_color).convert_alpha() # Cria a superfície do texto
        text_rect = Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1]) # Cria o retângulo do texto
        self.window.blit(source=text_surf, dest=text_rect) # Desenha o texto na janela