#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import pygame  # type: ignore[import]
except ImportError as e:
    raise ImportError("pygame is required to run this game. Install it with 'pip install pygame'.") from e

from code.const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.level import Level
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: # NEW GAME 1P, NEW GAME 2P - COOPERATIVE, NEW GAME 2P - COMPETITIVE
                player_score = [0, 0] # Inicializa a pontuação dos jogadores como 0
                level = Level(self.window, 'Level1', menu_return, player_score) # Cria o nível 1
                level_return = level.run(player_score) # Roda o nível 1
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                     
            elif menu_return == MENU_OPTION[4]: # EXIT
                pygame.quit() # Close window
                quit() # end pygame
            else: 
                pass
                
            


