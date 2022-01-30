from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectUseInWorkshopMessage(NetworkMessage):
    protocolId = 5412
    objectUID:int
    quantity:int
    
