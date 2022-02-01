from enum import Enum

class ProgressEvent(Enum):
    SOCKET_DATA = "socketData"
    
    def __init__(self, data):
        self.data = data