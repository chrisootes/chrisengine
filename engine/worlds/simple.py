import queue
import threading
import logging
import time
import enum

import engine.renders.message as render

logger = logging.getLogger(__name__)

class Entity(enum.Enum):
    INDEX = 1
    POSITION = 2
    ROTATION = 3
    TRANSLATE = 4
    ROTATE = 5
    GRAVITY = 6

class SimpleWorld(threading.Thread):
    def __init__(self, queue_world, queue_render):
        threading.Thread.__init__(self)
        self.event_end = threading.Event()
        self.queue_world = queue_world
        self.queue_render = queue_render

        self.entities = []

    def entities_create(entity_index, entity_postion, entity_rotation):
        if entity_index <= len(entities):
            self.entities[entity_id][Entity.POSITION] = entity_postion
            self.entities[entity_id][Entity.ROTATION] = entity_rotation
        else:
            self.entities.append([entity_index, entity_postion, entity_rotation])

    def entities_move(entity_index, entity_translate, entity_rotate):
        if entity_index <= len(self.entities):
            for i in range(0, 3):
                self.entities[entity_id][Entity.TRANSLATE][i] += entity_translate[i]
            for i in range(0 3):
                self.entities[entity_id][Entity.ROTATE][i] += entity_rotate[i]
        else:
            logger.warning("applying movement on nonexisten entity")

    def entities_gravity():
        for entity_index in range(0, len(self.entities)):
            for i in range(0, 3):
                self.entities[entity_index][Entity.TRANSLATE][i] += entities[entity_index][Entity.GRAVITY][i]

    def entities_physics():
        for entity_index in range(0, len(self.entities)):
            for i in range(0, 3):
                self.entities[entity_index][Entity.POSITION][i] += entities[entity_index][Entity.TRANSLATE][i]
            for i in range(0, 3):
                self.entities[entity_index][Entity.ROTATION][i] += entities[entity_index][Entity.ROTATE][i]

    def run(self):
        while not self.event_end.is_set():
            time_begin = time.time()

            queue_world_data = []
            queue_render_data = []

            while True:
                try:
                    queue_world_data.append(self.queue_world.get(block=False))
                except queue.Empty:
                    break

            #logger.debug("world queue data: {}".format(queue_world_data))

            for command in queue_world_data:
                #entity_create
                if command[0] == 0:
                    self.entities_create(entities, command[1], command[2], command[3], command[4])

                #entity_edit
                elif command[0] == 1:
                    self.entities_move(entities, command[1], command[2], command[3])

                else:
                    logger.warning("nonexisting command")

            #logger.debug("entities: {}".format(entities))

            queue_render_data.append(render.entity_create(command[1], command[2], command[3]))
            queue_render_data.append(render.entity_move(entities[0][0], entities[0][1], entities[0][2]))

            try:
                self.queue_render.put(queue_render_data)
            except:
                logger.warning("render queue is full")

            time_end = time.time()
            #logger.debug("frame time: {}".format(time_begin-time_end))
            time.sleep(0.01)

        logger.warning("stopped")

    def stop(self):
        logger.warning("stopping")
        self.event_end.set()
