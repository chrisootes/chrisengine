def entity_create(entity_index, entity_position, entity_rotation, entity_translate, entity_rotate, entity_gravity):
    return [0, entity_index, entity_position, entity_rotation, entity_translate, entity_rotate, entity_gravity]

def entity_move(entity_index, entity_translate, entity_rotate):
    return [1, entity_index, entity_translate, entity_rotate]
