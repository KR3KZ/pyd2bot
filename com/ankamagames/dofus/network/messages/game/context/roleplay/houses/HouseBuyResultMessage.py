from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseBuyResultMessage(NetworkMessage):
    houseId:int
    instanceId:int
    realPrice:int
    secondHand:bool
    bought:bool
    
    
