#!/usr/bin/python
# -*- coding: utf-8 -*-

from code import background
import random
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name: # Verifica o nome da entidade e retorna a entidade correspondente
            case 'level1bg': # Se for o background do nível 1, retorna uma lista de backgrounds para o nível 1
                list_bg = [] # Cria uma lista vazia para armazenar os backgrounds do nível 1
                for i in range(7): # Cria 7 backgrounds para o nível 1, cada um com um nome diferente (level1bg0, level1bg1, ..., level1bg6) e a mesma posição
                    list_bg.append(Background(f'level1bg{i}', position)) # Adiciona o background criado à lista de backgrounds do nível 1
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0))) # Adiciona um segundo background com a mesma imagem, mas posicionado à direita do primeiro, para criar um efeito de scrolling infinito
                return list_bg # Retorna a lista de backgrounds do nível 1
            case 'Player1':
                return Player(name = 'Player1', position = (10, WIN_HEIGHT / 2 - 30)) 
            case 'Player2':
                return Player(name = 'Player2', position = (10, WIN_HEIGHT / 2 + 30)) 
            case 'Enemy1':
                return Enemy('Enemy1', position=(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', position=(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))