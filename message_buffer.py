import logging
import threading
from message import Message
from logical_clock import LogicalClock
from typing import List

class MessageBuffer:
    def __init__(self):
        self.buffer = []
        self.lock = threading.Lock()
        self.clock = LogicalClock()
        self.log = []
    
    def add_message(self, message: Message):
        with self.lock:
            self.clock.update(message.timestamp)
            self.buffer.append(message)
            self.buffer.sort(key=lambda m: m.timestamp)
            
            log_entry = f"PRODUCED: {message}"
            self.log.append(log_entry)
            logging.info(log_entry)
    
    def get_message(self, consumer_id: str) -> Message:
        with self.lock:
            if not self.buffer:
                return None
            
            message = self.buffer.pop(0)
            consumption_time = self.clock.increment()
            message.consumption_time = consumption_time
            
            log_entry = f"CONSUMED: by {consumer_id}, {message}"
            self.log.append(log_entry)
            logging.info(log_entry)
            
            return message
    
    def get_log(self) -> List[str]:
        return self.log.copy()