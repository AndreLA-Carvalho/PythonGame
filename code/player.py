#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed() # Obtém as teclas pressionadas
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: # Se a tecla de seta para cima for pressionada e o jogador não estiver no topo da tela, move o jogador para cima
            self.rect.centery -= ENTITY_SPEED[self.name] # Move o jogador para cima
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: # Se a tecla de seta para baixo for pressionada e o jogador não estiver no fundo da tela, move o jogador para baixo
            self.rect.centery += ENTITY_SPEED[self.name] # Move o jogador para baixo
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0: # Se a tecla de seta para esquerda for pressionada e o jogador não estiver na borda esquerda da tela, move o jogador para esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name] # Move o jogador para esquerda
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH: # Se a tecla de seta para direita for pressionada e o jogador não estiver na borda direita da tela, move o jogador para direita
            self.rect.centerx += ENTITY_SPEED[self.name] # Move o jogador para direita
        pass
