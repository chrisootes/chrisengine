import queue
import threading
import logging
import time

logger = logging.getLogger(__name__)

class SimplePhysics(threading.Thread):
    def __init__(self, queue_physics, queue_world):
        threading.Thread.__init__(self)
        self.end = threading.Event()
        self.queue_physics = queue_physics
        self.queue_world = queue__world

    def run(self):
        while not self.end.is_set():
            #check physics
            time.sleep(0.1)

    def stop(self):
        logger.warning("stopping")
        self.end.set()
