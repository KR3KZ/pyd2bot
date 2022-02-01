from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountSterilizeFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    sterilizator:str
    
    
