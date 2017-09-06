import queue
import threading
import logging
import time

from engine.renders.message import object_edit

logger = logging.getLogger(__name__)

class SimpleWorld(threading.Thread):
    def __init__(self, queue_world, queue_render):
        threading.Thread.__init__(self)
        self.event_end = threading.Event()
        self.queue_world = queue_world
        self.queue_render = queue_render

    def run(self):
        camera_id = 0
        entities = [[camera_id, [0.0,0.0,0.0], [0.0,0.0,0.0]]]

        while not self.event_end.is_set():
            queue_world_data = []
            while True:
                try:
                    queue_world_data.append(self.queue_world.get(block=False))
                except queue.Empty:
                    break

            #logger.debug("world queue data: {}".format(queue_world_data))

            for command in queue_world_data:
                if command[0] == 0:
                    entities.append([command[1], command[2], command[3]])
                elif command[0] == 1:
                    if command[2] != None:
                        for i in range(0,3):
                            entities[command[1]][1][i] = command[2][i]
                    if command[3] != None:
                        for i in range(0,3):
                            entities[command[1]][1][i] += command[3][i]
                    if command[4] != None:
                        for i in range(0,3):
                            entities[command[1]][2][i] = command[4][i]
                    if command[5] != None:
                        for i in range(0,3):
                            entities[command[1]][2][i] += command[5][i]

            #logger.debug("entities: {}".format(entities))

            queue_render_data = object_edit(entities[0][0], entities[0][1], entities[0][2])

            try:
                self.queue_render.put(queue_render_data)
            except:
                logger.warning("render queue is full")

            time.sleep(0.01)

        logger.warning("stopped")

    def stop(self):
        logger.warning("stopping")
        self.event_end.set()
