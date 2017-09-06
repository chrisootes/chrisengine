def entity_create(entity_index, entity_position, entity_rotation):
    return [0, entity_index, entity_position, entity_rotation]

def entity_move(entity_index, entity_translate, entity_rotate):
    return [1, entity_index, entity_translate, entity_rotate]

def camera_set(relative_position, relative_rotation):
    return [2, relative_position, relative_rotation]
