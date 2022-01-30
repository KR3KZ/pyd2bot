from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChatAbstractServerMessage(INetworkMessage):
    protocolId = 3393
    channel:int
    content:str
    timestamp:int
    fingerprint:str
    
    
