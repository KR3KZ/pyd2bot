from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockBuyResultMessage(NetworkMessage):
    protocolId = 6835
    paddockId:int
    bought:bool
    realPrice:int
    
    
