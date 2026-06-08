#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

import pygame.image

from code.const import ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SCORE


class Entity(ABC): 
    def __init__(self, name: str, position: tuple): # name: nome da entidade, position: posição inicial da entidade (x, y)
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() # Carrega a imagem da entidade e converte para alpha para permitir transparência
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # Define a posição do sprite na tela
        self.speed = 0
        self.health = ENTITY_HEALTH[name] # Define a saúde da entidade com base no nome da entidade
        self.damage = ENTITY_DAMAGE[self.name] # Define o dano da entidade com base no nome da entidade
        self.score = ENTITY_SCORE[self.name] # Define a pontuação da entidade com base no nome da entidade
        self.last_dmg = 'None' # Define a última entidade que causou dano a esta entidade, inicialmente 'None'

    @abstractmethod
    def move(self, ):
        pass
