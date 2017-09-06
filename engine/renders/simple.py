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
        'main render loop'
        init_screen()
        init_opengl()

        entities = []

        #lists
        floor_id = list_file('./floor.msh')
        obj_id = list_file('./obj.msh')

        while not self.event_end.is_set():s
            time_begin = time.time()

            #get queue
            queue_render_data = []

            while True:
                try:
                    queue_render_data.append(self.queue_render.get(block=False))
                except queue.Empty:
                    break


            #logger.debug("render queue data: {}".format(queue_render_data))

            #update entities positions
            for command in queue_render_data:
                if command[0] == 0:
                    entities.append([command[1], command[2], command[3]])

                elif command[0] == 1:
                    if command[2] != None:
                        for i in range(0,3):
                            entities[command[1]][1][i] = command[2][i]
                    if command[3] != None:
                        for i in range(0,3):
                            entities[command[1]][2][i] = command[3][i]

            logger.debug("entities: {}".format(entities))

            #render entities
            for entity in entities:
                if entity[0] == 0:
                    #render camera
                    camera_loop(entity[2][0], entity[2][1])

                elif entity[0] == 1:
                    #set glLight
                    light_loop(entity[1][0], entity[1][1], entity[1][2])

                else:
                    pass

            #render all
            render_obj(obj_id, 0.1)
            render_floor(floor_id)

            #flip
            update_screen()

            #limit frames
            time.sleep(0.01)

        logger.warning("stopped")

    def stop(self):
        logger.warning("stopping")
        self.event_end.set()
