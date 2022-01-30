from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DecraftedItemStackInfo(NetworkMessage):
    protocolId = 8215
    objectUID:int
    bonusMin:int
    bonusMax:int
    runesId:int
    runesQty:int
    
