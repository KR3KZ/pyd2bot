from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeObjectUseInWorkshopMessage(INetworkMessage):
    protocolId = 5412
    objectUID:int
    quantity:int
    
    
