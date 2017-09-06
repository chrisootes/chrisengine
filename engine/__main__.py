import sys
import logging
import argparse
import queue
import threading
import time

from engine.games.simple import SimpleGame
from engine.inputs.simple import SimpleInput
#from engine.worlds.simple import SimpleWorld
#from engine.renders.simple import SimpleRender

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("loading")

    #queue
    queue_world = queue.Queue()
    queue_render = queue.Queue()

    #game
    game_thread = SimpleGame(queue_world)
    game_thread.start()

    #input
    input_thread = SimpleInput(queue_world)
    input_thread.start()

    #world
    #world_thread = SimpleWorld(queue_world, queue_render)
    #world_thread.start()

    #render
    #render_thread = SimpleRender(queue_render)
    #render_thread.start()

    logger.info("sleeping")
    time.sleep(20)

    game_thread.stop()
    game_thread.join()
    input_thread.stop()
    input_thread.join()
    #world_thread.stop()
    #world_thread.join()
    #render_thread.stop()
    #render_thread.join()

    logger.info("exiting")
    return 0

if __name__ == '__main__':
    sys.exit(main())
