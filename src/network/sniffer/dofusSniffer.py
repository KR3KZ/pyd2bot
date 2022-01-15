#!/usr/bin/env python3
import json
import socket
from scapy.all import AsyncSniffer, Packet
import logging
from ..message import Buffer, Msg


IGNORED_MSGS = ["ChatServerMessage", 
                "ChatServerWithObjectMessage", 
                "GameMapMovementMessage", 
                "BasicLatencyStatsMessage", 
                "BasicNoOperationMessage", 
                "BasicLatencyStatsRequestMessage"]

bot_map_json_path = r"C:\Users\majdoub\OneDrive\Documents\bot2pix\map.json"

class DofusSniffer(AsyncSniffer):
    
    def __init__(self, action, capture_file, bot=None):
        super().__init__(
        filter="tcp port 5555",
        prn=lambda pkt: self.onReceive(pkt, action),
        offline=capture_file)
        self.LOCAL_IP = self.getLocalIp()
        self.SERVER_IP = None
        self.fromClientBuffer = Buffer()
        self.fromServerBuffer = Buffer()
        self.bot=None
    
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
        logging.debug("Determining packet origin...")
        dst = pa.getlayer('IP').dst
        src = pa.getlayer('IP').src
        if src == self.LOCAL_IP:
            logging.debug("Packet comes from local machine")
            return True
        elif dst == self.LOCAL_IP:
            logging.debug("Packet comes from server")
            if not self.SERVER_IP:
                self.SERVER_IP = src
            return False
        logging.error(
            "Packet origin unknown\nsrc: %s\ndst: %s\nLOCAL_IP: %s", src, dst, self.LOCAL_IP
        )
        raise Exception("Packet origin unknown")

    def onReceive(self, pa: Packet, action):
        logging.debug("Received packet. ")
        if pa and pa.haslayer('TCP'):
            isfromClient = self.isFromClient(pa)
            buf = self.fromClientBuffer if isfromClient else self.fromServerBuffer
            raw_pa = pa.getlayer('Raw')
            if raw_pa:
                buf += raw_pa.load
                msg = Msg.fromRaw(buf, isfromClient)
                while msg:
                    if msg.msgType["name"] not in IGNORED_MSGS:
                        action(msg)
                        if self.bot:
                            self.bot.handleMsg(msg)
                    msg = Msg.fromRaw(buf, isfromClient)
        