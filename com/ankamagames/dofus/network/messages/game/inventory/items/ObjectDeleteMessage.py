from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectDeleteMessage(INetworkMessage):
    protocolId = 8147
    objectUID:int
    quantity:int
    
    
