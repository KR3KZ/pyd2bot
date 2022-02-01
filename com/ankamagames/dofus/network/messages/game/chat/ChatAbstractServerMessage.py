from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatAbstractServerMessage(NetworkMessage):
    channel:int
    content:str
    timestamp:int
    fingerprint:str
    
    
