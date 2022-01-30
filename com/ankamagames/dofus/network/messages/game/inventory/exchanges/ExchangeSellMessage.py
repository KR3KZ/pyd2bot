from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeSellMessage(INetworkMessage):
    protocolId = 5196
    objectToSellId:int
    quantity:int
    
    
