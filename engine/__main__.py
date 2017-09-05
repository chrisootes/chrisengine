import sys
import logging
import argparse
import queue
import threading
import time

from engine.inputs.simple import SimpleInput
from engine.worlds.simple import SimpleWorld
from engine.renders.simple import SimpleRender

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO)
    logger.info("loading")

    #queue
    queue_physics = queue.Queue()
    queue_world = queue.Queue()
    queue_render = queue.Queue()

    #input
    input_thread = SimpleInput(queue_world)
    input_thread.start()

    #world
    world_thread = SimpleWorld(queue_world, queue_render)
    world_thread.start()

    #render
    render_thread = SimpleRender(queue_render)
    render_thread.start()

    time.sleep(10)
    input_thread.stop()
    world_thread.stop()
    render_thread.stop()

if __name__ == '__main__':
    sys.exit(main())
