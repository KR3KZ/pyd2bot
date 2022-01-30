from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftResultMessage(NetworkMessage):
    protocolId = 8524
    craftResult:int
    
