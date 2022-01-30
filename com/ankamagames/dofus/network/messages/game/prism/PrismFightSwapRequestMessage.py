from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismFightSwapRequestMessage(INetworkMessage):
    protocolId = 4070
    subAreaId:int
    targetId:int
    
    
