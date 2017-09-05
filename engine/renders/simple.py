import queue
import threading
import logging
import time

from engine.renders.opengl import *

logger = logging.getLogger(__name__)

class SimpleRender(threading.Thread):
    def __init__(self, queue_render):
        threading.Thread.__init__(self)

        self.event_end = threading.Event()
        self.queue_render = queue_render

    def run(self):
        'main loop'

        init_screen()
        init_opengl()

        #lists
        floor_id = list_file('./floor.msh')
        obj_id = list_file('./obj.msh')

        while not self.event_end.is_set():
            #render camera
            camera_loop()

            #set glLight
            light_loop()

            #render all
            render_obj(obj_id, 0.1)
            render_floor(floor_id)

            #flip
            update_screen()

    def stop(self):
        logger.warning("stopping")
        self.event_end.set()
