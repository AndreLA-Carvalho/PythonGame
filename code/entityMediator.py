from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:
    
    @staticmethod
    def __verify_collision_window(ent: Entity): # Verifica colisão da entidade com a janela e remove a saúde da entidade se ela colidir com a janela
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        

    @staticmethod
    def verify_collision(entity_list: list[Entity]): # Verifica colisões entre as entidades e com a janela
        for i in range(len(entity_list)):
            test_entity = entity_list[i] 
            EntityMediator.__verify_collision_window(test_entity) # Verifica colisão com a janela
            
    @staticmethod
    def verify_health(entity_list: list[Entity]): # Verifica a saúde das entidades e remove as que tiverem saúde menor ou igual a 0
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent) # Remove a entidade da lista de entidades se a saúde for menor ou igual a 0