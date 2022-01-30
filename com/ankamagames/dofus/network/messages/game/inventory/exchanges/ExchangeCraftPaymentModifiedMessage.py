from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeCraftPaymentModifiedMessage(INetworkMessage):
    protocolId = 8641
    goldSum:int
    
    
