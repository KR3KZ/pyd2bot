from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectQuantityMessage(INetworkMessage):
    protocolId = 80
    objectUID:int
    quantity:int
    origin:int
    
    
