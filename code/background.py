#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Move o background para a esquerda a cada frame
        if self.rect.right <= 0:  # Se o background sair completamente da tela pela esquerda, reposiciona-o à direita para criar um efeito de scrolling infinito
            self.rect.left = WIN_WIDTH  # Reposiciona o background à direita da tela
