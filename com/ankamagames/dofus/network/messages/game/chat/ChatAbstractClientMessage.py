from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatAbstractClientMessage(NetworkMessage):
    protocolId = 1037
    content:str
    
    
