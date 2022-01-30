from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TitleSelectedMessage(INetworkMessage):
    protocolId = 8922
    titleId:int
    
    
