from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeHandleMountsMessage(NetworkMessage):
    actionType:int
    ridesId:list[int]
    
    
