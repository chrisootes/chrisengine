import queue
import threading
import logging
import time

from engine.types.entity import GameEntity

logger = logging.getLogger(__name__)

class SimpleWorld(threading.Thread):
    def __init__(self, queue_world, queue_render):
        threading.Thread.__init__(self)
        self.event_end = threading.Event()
        self.queue_world = queue_world
        self.queue_render = queue_render

        camera = GameEntity(0)
        self.entities = [camera]

    def run(self):
        while not self.event_end.is_set():
            #check world queue
            try:
                queue_data = self.queue_world.get(block=False)
                logger.info("world queue {}".format(queue_data))
                self.entities[queue_data[0]].anim = queue_data[1]
            except queue.Empty:
                pass

            #calculate animations
            for entity in self.entities:
                entity.animate()

            #give render queue
            try:
                queue_data = []
                self.queue_render.put(queue)
            except:
                logger.warning("render queue is full")

            time.sleep(0.1)

    def stop(self):
        logger.warning("stopping")
        self.event_end.set()
