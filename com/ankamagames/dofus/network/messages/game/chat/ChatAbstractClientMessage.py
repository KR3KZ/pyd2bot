from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChatAbstractClientMessage(INetworkMessage):
    protocolId = 1037
    content:str
    
    
