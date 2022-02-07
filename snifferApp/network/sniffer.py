import socket
from time import sleep
from scapy.all import AsyncSniffer, Packet
from com.ankamagames.jerakine.network.CustomDataWrapper import Buffer
from .message import Message
import signal
class DofusSniffer(AsyncSniffer):
    
    def __init__(self, action, capture_file=None):
        super().__init__(
            filter="tcp port 5555",
            prn=lambda pkt: self.onReceive(pkt, action),
            offline=capture_file
        )
        self.LOCAL_IP = self.getLocalIp()
        self.AUTH_SERVER_IP = None
        self.fromClientBuffer = Buffer()
        self.fromServerBuffer = Buffer()
    
    def getLocalIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("10.255.255.255", 1))
            local_ip = s.getsockname()[0]
        except:
            local_ip = "127.0.0.1"
        finally:
            s.close()
        return local_ip

    def isFromClient(self, pa: Packet):
        dst = pa.getlayer('IP').dst
        src = pa.getlayer('IP').src
        if src == self.LOCAL_IP:
            return True
        elif dst == self.LOCAL_IP:
            return False
        raise Exception(f"Packet origin unknown\nsrc: {src}\ndst: {dst}\nLOCAL_IP: {self.LOCAL_IP}")

    def onReceive(self, pa: Packet, handle):
        dst = pa.getlayer('IP').dst
        src = pa.getlayer('IP').src
        if pa and pa.haslayer('TCP'):
            isfromClient = self.isFromClient(pa)
            buf = self.fromClientBuffer if isfromClient else self.fromServerBuffer
            raw_layer = pa.getlayer('Raw')
            if raw_layer:
                buf += raw_layer.load
                while True:
                    msg = Message.fromRaw(buf, isfromClient, src=src, dst=dst)
                    if not msg:
                        break
                    handle(msg)
                    
if __name__  == "__main__":
    def handle(msgRaw:Message):
        msg = msgRaw.deserialize()
        if msgRaw.from_client:
            print(">>>>>>>>>>>> " + str(msg))
        else:
            print("<<<<<<<<<<<< " + str(msg))
    mySniffer = DofusSniffer(handle)
    mySniffer.start()
    signal.signal(signal.SIGINT, mySniffer.stop)
    mySniffer.join()