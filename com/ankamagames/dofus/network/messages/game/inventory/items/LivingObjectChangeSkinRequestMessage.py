from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LivingObjectChangeSkinRequestMessage(INetworkMessage):
    protocolId = 7679
    livingUID:int
    livingPosition:int
    skinId:int
    
    
