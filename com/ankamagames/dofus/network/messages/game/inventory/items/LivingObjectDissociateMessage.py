from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LivingObjectDissociateMessage(INetworkMessage):
    protocolId = 9254
    livingUID:int
    livingPosition:int
    
    
