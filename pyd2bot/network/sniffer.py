import socket
from scapy.all import AsyncSniffer, Packet
from .message import Msg
from pyd2bot.utils.binaryIO import Buffer

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
                    msg = Msg.fromRaw(buf, isfromClient, src=src, dst=dst)
                    if not msg:
                        break
                    print(f"Received msg. {msg.json()['__type__']}, src {src} -> dst: {dst}")
                    if msg.name == "RawDataMessage":
                        with open(r"C:\Users\majdoub\OneDrive\Documents\pyd2bot\tests\rawd.bin", 'wb') as fp:
                            fp.write(msg.json()["content"])
                    handle(msg)
                    

        