from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeMountFreeFromPaddockMessage(INetworkMessage):
    protocolId = 4810
    name:str
    worldX:int
    worldY:int
    liberator:str
    
    
