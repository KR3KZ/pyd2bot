from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeMountFreeFromPaddockMessage(INetworkMessage):
    protocolId = 4810
    name:str
    worldX:int
    worldY:int
    liberator:str
    
    
