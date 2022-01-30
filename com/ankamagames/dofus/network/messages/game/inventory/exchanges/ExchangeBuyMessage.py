from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBuyMessage(INetworkMessage):
    protocolId = 9589
    objectToBuyId:int
    quantity:int
    
    
