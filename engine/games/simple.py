import queue
import threading
import logging
import time
import math

import engine.worlds.message as world

logger = logging.getLogger(__name__)

class SimpleGame(threading.Thread):
    def __init__(self, queue_world):
        threading.Thread.__init__(self)
        self.event_end = threading.Event()
        self.queue_world = queue_world

    def run(self):
        camera_id = 0
        light_id = 1
        queue_world_data = []

        queue_world_data.append(world.entity_create(camera_id, [0.0,10.0,0.0], [0.0,0.0,0.0], [0.0,0.0,0.0], [0.0,0.0,0.0], [0.0,-1.0,0.0]))
        queue_world_data.append(world.entity_create(light_id, [0.0,20.0,0.0], [0.0,0.0,0.0], [0.0,0.0,0.0], [0.0,0.0,0.0], [0.0,0.0,0.0]))

        logger.warning("stopped")

    def stop(self):
        logger.warning("stopping")
        self.event_end.set()
