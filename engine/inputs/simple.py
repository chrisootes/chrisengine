import queue
import threading
import logging
import time
import math
import win32api

import engine.worlds.message as world

logger = logging.getLogger(__name__)

class SimpleInput(threading.Thread):
    def __init__(self, queue_world):
        threading.Thread.__init__(self)
        self.event_end = threading.Event()
        self.queue_world = queue_world

    def run(self):
        player_id = 0

        x_res = 1920
        y_res = 1080

        x_old = x_res/2
        y_old = y_res/2

        key_forward = 87
        key_backward = 83

        while not self.event_end.is_set():
            time_begin = time.time()

            translate = [0.0,0.0,0.0]
            rotate = [0.0,0.0,0.0]

            x_new, y_new = win32api.GetCursorPos()
            #logger.debug("x: {}, y: {}".format(x_new, y_new))

            rotate[0] = (x_old - x_new) / x_res
            rotate[1] = (y_old - y_new) / y_res

            logger.debug("rotate: {}".format(rotate))

            event_forward = win32api.GetKeyState(87)
            #logger.debug("forward: {}".format(event_forward))

            if event_forward == -127 or event_forward == -128:
                translate[0] = -1.0

            event_backward = win32api.GetKeyState(key_backward)
            #logger.debug("backward: {}".format(event_backward))

            if event_backward == -127 or event_backward == -128:
                translate[0] = -1.0

            queue_world_data = world.entity_move(camera_id, translate, rotate)
            #logger.debug("world queue data: {}".format(queue_world_data))

            try:
                self.queue_world.put(queue_world_data, block=False)
            except:
                logger.warning("world queue is full")

            time_end = time.time()
            #logger.debug("frame time: {}".format(time_begin-time_end))
            time.sleep(0.01)

        logger.warning("stopped")

    def stop(self):
        logger.warning("stopping")
        self.event_end.set()
