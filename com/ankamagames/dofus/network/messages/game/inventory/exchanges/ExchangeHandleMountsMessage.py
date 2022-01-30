from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeHandleMountsMessage(NetworkMessage):
    protocolId = 9421
    actionType:int
    ridesId:int
    
