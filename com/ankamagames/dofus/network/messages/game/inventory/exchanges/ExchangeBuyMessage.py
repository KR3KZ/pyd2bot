from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBuyMessage(NetworkMessage):
    protocolId = 9589
    objectToBuyId:int
    quantity:int
    
    
