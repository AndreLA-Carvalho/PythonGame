from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.player import Player
from code.playerShot import PlayerShot


class EntityMediator:

# Verifica colisão da entidade com a janela e remove a saúde da entidade se ela colidir com a janela    
    @staticmethod
    def __verify_collision_window(ent: Entity): # Verifica colisão da entidade com a janela e remove a saúde da entidade se ela colidir com a janela
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0
         
# Verifica colisão entre as entidades e remove a saúde das entidades se elas colidirem                
    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        
        if valid_interaction: # if valid_interaction == True
            if ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom: # Verifica colisão entre as entidades
                ent1.health -= ent2.damage # Remove a saúde da entidade 1 com base no dano da entidade 2
                ent2.health -= ent1.damage # Remove a saúde da entidade 2 com base no dano da entidade 1
                ent1.last_dmg = ent2.name # Define a última entidade que causou dano a entidade 1 como a entidade 2
                ent2.last_dmg = ent1.name # Define a última entidade que causou dano a entidade 2 como a entidade 1
                
# Dá pontos para o jogador com base no tipo do inimigo morto
    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]): # Dá pontos para o jogador com base no tipo do inimigo morto
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

# Verifica colisões entre as entidades e com a janela, e verifica a saúde das entidades e remove as que tiverem saúde menor ou igual a 0
    @staticmethod
    def verify_collision(entity_list: list[Entity]): # Verifica colisões entre as entidades e com a janela
        for i in range(len(entity_list)):
            entity1 = entity_list[i] # Verifica colisão da entidade com a janela e remove a saúde da entidade se ela colidir com a janela
            EntityMediator.__verify_collision_window(entity1) # Verifica colisão com a janela
            for j in range(i+1, len(entity_list)): # Verifica colisão entre as entidades e remove a saúde das entidades se elas colidirem
                entity2 = entity_list[j] 
                EntityMediator.__verify_collision_entity(entity1, entity2) 

# Verifica a saúde das entidades e remove as que tiverem saúde menor ou igual a 0            
    @staticmethod
    def verify_health(entity_list: list[Entity]): # Verifica a saúde das entidades e remove as que tiverem saúde menor ou igual a 0
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list) # Dá pontos para o jogador com base no tipo do inimigo morto
                entity_list.remove(ent) # Remove a entidade da lista de entidades se a saúde for menor ou igual a 0