from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockBuyResultMessage(NetworkMessage):
    paddockId:int
    bought:bool
    realPrice:int
    
    
