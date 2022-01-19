#!/usr/bin/env python3
import json
import socket
from scapy.all import AsyncSniffer, Packet
import logging
from ..message import Buffer, Msg


# IGNORED_MSGS = [
#     # chat msgs to ignore
#     "ChatServerMessage", 
#     "ChatServerWithObjectMessage", 
    
#     # map msgs to ignore
#     "GameMapMovementMessage", 
#     "BasicLatencyStatsMessage", 
#     "BasicNoOperationMessage", 
#     "BasicLatencyStatsRequestMessage",
#     "ListMapNpcsQuestStatusUpdateMessage",
#     "MapInformationsRequestMessage",
#     "MapRewardRateMessage",
#     "UpdateMapPlayersAgressableStatusMessage",
#     "SetCharacterRestrictionsMessage",
#     "BasicTimeMessage",
#     "PrismsListUpdateMessage",
    
#     # job msgs to ignore
#     "ObtainedItemWithBonusMessage",
#     "JobExperienceUpdateMessage",
#     "ObjectQuantityMessage",
    
#     # fight msgs to ignore
#     "CharacterStatsListMessage",
#     "GameFightPlacementPossiblePositionsMessage",
#     "GameFightOptionStateUpdateMessage",
#     "IdolFightPreparationUpdateMessage",
#     "LifePointsRegenEndMessage"
# ]
IGNORED_MSGS = []
class DofusSniffer(AsyncSniffer):
    
    def __init__(self, action, capture_file=None):
        super().__init__(
            filter="tcp port 5555",
            prn=lambda pkt: self.onReceive(pkt, action),
            offline=capture_file
        )
        self.LOCAL_IP = self.getLocalIp()
        self.SERVER_IP = None
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
            print(src)
            if not self.SERVER_IP:
                self.SERVER_IP = src
            return False
        raise Exception(f"Packet origin unknown\nsrc: {src}\ndst: {dst}\nLOCAL_IP: {self.LOCAL_IP}")

    def onReceive(self, pa: Packet, handle):
        logging.debug("Received packet. ")
        if pa and pa.haslayer('TCP'):
            isfromClient = self.isFromClient(pa)
            buf = self.fromClientBuffer if isfromClient else self.fromServerBuffer
            raw_layer = pa.getlayer('Raw')
            if raw_layer:
                buf += raw_layer.load
                msg = Msg.fromRaw(buf, isfromClient)
                while msg:
                    if msg.msgType["name"] not in IGNORED_MSGS:
                        handle(msg)
                    msg = Msg.fromRaw(buf, isfromClient)


        