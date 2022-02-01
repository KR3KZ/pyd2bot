from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeOkMultiCraftMessage(NetworkMessage):
    initiatorId:int
    otherId:int
    role:int
    
    
