import queue
import threading
import logging
import time

import inputs

logger = logging.getLogger(__name__)

class SimpleInput(threading.Thread):
    def __init__(self, queue_world):
        threading.Thread.__init__(self)
        self.event_end = threading.Event()
        self.queue_world = queue_world

        self.keys = {
            'KEY_W': {
                'state': 0,
                'entity': 0,
                0: 'still',
                1: 'forward'
            },
            'KEY_S': {
                'state': 0,
                'entity': 0,
                0: 'still',
                1: 'backward'
            }
        }

    def run(self):
        while not self.event_end.is_set():
            events = inputs.get_key()
            for event in events:
                logger.debug("type: {}, code: {}, stat: {}".format(event.ev_type, event.code, event.state))
                if event.code in self.keys:
                    key = self.keys[event.code]
                    if key['state'] != event.state:
                        self.keys[event.code]['state'] = event.state
                        try:
                            queue_data = [key['entity'], key[event.state]]
                            logger.info("world queue {}".format(queue_data))
                            self.queue_world.put(queue_data, block=False)
                        except:
                            logger.warning("world queue is full")

    def stop(self):
        logger.warning("stopping")
        self.event_end.set()
