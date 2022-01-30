from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DecraftedItemStackInfo(INetworkMessage):
    protocolId = 8215
    objectUID:int
    bonusMin:int
    bonusMax:int
    runesId:int
    runesQty:int
    
    
