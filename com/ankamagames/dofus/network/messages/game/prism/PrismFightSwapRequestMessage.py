from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismFightSwapRequestMessage(NetworkMessage):
    protocolId = 4070
    subAreaId:int
    targetId:float
    
