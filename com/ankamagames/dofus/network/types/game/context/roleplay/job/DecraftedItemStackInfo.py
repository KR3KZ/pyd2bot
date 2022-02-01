from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DecraftedItemStackInfo(NetworkMessage):
    objectUID:int
    bonusMin:int
    bonusMax:int
    runesId:list[int]
    runesQty:list[int]
    
    
