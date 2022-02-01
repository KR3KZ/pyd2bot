from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LivingObjectChangeSkinRequestMessage(INetworkMessage):
    protocolId = 7679
    livingUID:int
    livingPosition:int
    skinId:int
    
    
