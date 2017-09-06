import queue
import threading
import logging
import time
import math
import win32api

from engine.worlds.message import object_edit

logger = logging.getLogger(__name__)

class SimpleInput(threading.Thread):
    def __init__(self, queue_world):
        threading.Thread.__init__(self)
        self.event_end = threading.Event()
        self.queue_world = queue_world

    def run(self):
        camera_id = 0
        rotation = [0.0,0.0,0.0]

        x_res = 1920
        y_res = 1080

        x_old = x_res/2
        y_old = y_res/2

        key_forward = 87
        key_backward = 83

        while not self.event_end.is_set():
            time_begin = time.time()

            translate = [0.0,0.0,0.0]

            x_new, y_new = win32api.GetCursorPos()
            #logger.debug("x: {}, y: {}".format(x_new, y_new))

            rotation[0] = (((x_old - x_new) / x_res) - 0.5) * 360.0
            x_old = x_res

            rotation[1] = (((y_old - y_new) / y_res) - 0.5) * 360.0
            y_old = y_res

            #logger.debug("rotation: {}".format(rotation))

            event_forward = win32api.GetKeyState(87)
            #logger.debug("forward: {}".format(event_forward))

            if event_forward == -127 or event_forward == -128:
                translate[1] -= math.sin(rotation[0])
                translate[2] += math.cos(rotation[0])

            event_backward = win32api.GetKeyState(key_backward)
            #logger.debug("backward: {}".format(event_backward))

            if event_backward == -127 or event_backward == -128:
                translate[1] += math.sin(rotation[0])
                translate[2] -= math.cos(rotation[0])

            queue_world_data = object_edit(camera_id, None, translate, rotation, None)
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
