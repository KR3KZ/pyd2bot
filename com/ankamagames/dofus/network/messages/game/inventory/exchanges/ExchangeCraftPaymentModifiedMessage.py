from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftPaymentModifiedMessage(NetworkMessage):
    protocolId = 8641
    goldSum:int
    
