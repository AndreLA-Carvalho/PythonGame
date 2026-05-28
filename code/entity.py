#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC): 
    def __init__(self, name: str, position: tuple): # name: nome da entidade, position: posição inicial da entidade (x, y)
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png') # Carrega a imagem do sprite com base no nome da entidade
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # Define a posição do sprite na tela
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
