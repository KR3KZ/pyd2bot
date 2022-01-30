from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeOkMultiCraftMessage(NetworkMessage):
    protocolId = 2595
    initiatorId:int
    otherId:int
    role:int
    
