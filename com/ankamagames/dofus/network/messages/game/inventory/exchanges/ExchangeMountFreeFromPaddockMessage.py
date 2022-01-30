from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountFreeFromPaddockMessage(NetworkMessage):
    protocolId = 4810
    name:str
    worldX:int
    worldY:int
    liberator:str
    
    
