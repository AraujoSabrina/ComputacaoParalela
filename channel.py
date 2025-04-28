from message_buffer import MessageBuffer;

class Channel:
    def __init__(self, name: str):
        self.name = name
        self.buffer = MessageBuffer()
        self.subscribers = set()