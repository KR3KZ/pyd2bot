from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectDropMessage(INetworkMessage):
    protocolId = 5971
    objectUID:int
    quantity:int
    
    
