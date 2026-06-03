#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.const import ENTITY_SHOT_DELAY, ENTITY_SPEED, WIN_WIDTH
from code.enemyShot import EnemyShot
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] # Define o tempo de delay entre os tiros do inimigo
        

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        
    def shoot(self):
        self.shot_delay -= 1 # Decrementa o tempo de delay entre os tiros do inimigo
        if self.shot_delay == 0: # Se o tempo de delay entre os tiros do inimigo for igual a 0, o inimigo pode atirar
            self.shot_delay = ENTITY_SHOT_DELAY[self.name] # Reinicia o tempo de delay entre os tiros do inimigo
            return EnemyShot(name = f'{self.name}Shot', position = (self.rect.centerx, self.rect.centery)) # Cria um tiro do inimigo na posição do inimigo