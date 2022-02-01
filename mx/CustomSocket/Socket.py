

import socket
from whistle import EventDispatcher
from com.ankamagames.jerakine.events.BasicEvent import BasicEvent
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


class Socket:

    def __init__(self, host, port):
        self.dispatcher = EventDispatcher()
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.host = host
        self.port = port
    
    def connect(self, host, port):
        self._sock.connect((host, port))
        self.connected = True
        self.dispatcher.dispatch(BasicEvent.CONNECT)

    def close(self):
        self._sock.close()
        self.connected = False
        self.dispatcher.dispatch(BasicEvent.CLOSE)

    def addEventListener(self, event, listener, priority=0, useWeakReference=False):
        self.dispatcher.add_listener(event, listener, priority)
    
    def removeEventListener(self, event, listener):
        self.dispatcher.remove_listener(event, listener)
    
    def dispatchEvent(self, event):
        self.dispatcher.dispatch(event)

    def send(self, data):
        self._sock.sendall(data)

    def receive(self, size=8192) -> ByteArray:
        return ByteArray(self._sock.recv(size))