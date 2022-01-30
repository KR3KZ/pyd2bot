from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DecraftedItemStackInfo(NetworkMessage):
    protocolId = 8215
    objectUID:int
    bonusMin:float
    bonusMax:float
    runesId:list[int]
    runesQty:list[int]
    
