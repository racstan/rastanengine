def check_collisions(entity_group1, entity_group2):
    collisions = pygame.sprite.groupcollide(entity_group1, entity_group2, False, False)
    return collisions
