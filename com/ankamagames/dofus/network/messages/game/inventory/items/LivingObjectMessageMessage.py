from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LivingObjectMessageMessage(INetworkMessage):
    protocolId = 2593
    msgId:int
    timeStamp:int
    owner:str
    objectGenericId:int
    
    
