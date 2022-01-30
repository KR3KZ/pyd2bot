from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountSterilizeFromPaddockMessage(NetworkMessage):
    protocolId = 2234
    name:str
    worldX:int
    worldY:int
    sterilizator:str
    
