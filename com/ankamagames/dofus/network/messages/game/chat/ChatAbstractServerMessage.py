from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatAbstractServerMessage(NetworkMessage):
    protocolId = 3393
    channel:int
    content:str
    timestamp:int
    fingerprint:str
    
    
