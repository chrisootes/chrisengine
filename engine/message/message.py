import sys
import logging
import queue
import threading

queue_struct = {

}

#TODO properties

def create_system():

def create_thread():

def get_messages():
    while True:
        try:
            queue_world_data.append(self.queue_world.get(block=False))
        except queue.Empty:
            break

def post_message():
    try:
        self.queue_render.put(queue_render_data)
    except:
        logger.warning("render queue is full")
