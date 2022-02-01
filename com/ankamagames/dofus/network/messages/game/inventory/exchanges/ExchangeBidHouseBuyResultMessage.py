from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyResultMessage(NetworkMessage):
    uid:int
    bought:bool
    
    
