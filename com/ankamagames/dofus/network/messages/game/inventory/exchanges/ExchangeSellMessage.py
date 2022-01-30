from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeSellMessage(NetworkMessage):
    protocolId = 5196
    objectToSellId:int
    quantity:int
    
    
