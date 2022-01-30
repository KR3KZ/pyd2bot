from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeObjectMoveMessage(INetworkMessage):
    protocolId = 5229
    objectUID:int
    quantity:int
    
    
