from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockBuyResultMessage(INetworkMessage):
    protocolId = 6835
    paddockId:int
    bought:bool
    realPrice:int
    
    
