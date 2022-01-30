from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountsTakenFromPaddockMessage(NetworkMessage):
    protocolId = 2526
    name:str
    worldX:int
    worldY:int
    ownername:str
    
