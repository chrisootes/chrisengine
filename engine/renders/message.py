def object_create(id, position = [0.0, 0.0, 0.0], rotation = [0.0, 0.0, 0.0]):
    return [0, id, position, rotation]

def object_edit(id, position = None, rotation = None):
    return [1, id, position, rotation]