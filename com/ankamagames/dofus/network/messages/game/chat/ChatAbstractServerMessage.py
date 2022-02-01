from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChatAbstractServerMessage(INetworkMessage):
    protocolId = 3393
    channel:int
    content:str
    timestamp:int
    fingerprint:str
    
    
