from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeMountSterilizeFromPaddockMessage(INetworkMessage):
    protocolId = 2234
    name:str
    worldX:int
    worldY:int
    sterilizator:str
    
    
