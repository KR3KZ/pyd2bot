from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectMoveMessage(NetworkMessage):
    protocolId = 5229
    objectUID:int
    quantity:int
    
    
