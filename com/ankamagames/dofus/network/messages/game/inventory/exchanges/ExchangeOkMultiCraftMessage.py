from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeOkMultiCraftMessage(NetworkMessage):
    protocolId = 2595
    initiatorId:float
    otherId:float
    role:int
    
