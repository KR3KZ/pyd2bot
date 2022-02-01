from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LivingObjectMessageRequestMessage(INetworkMessage):
    protocolId = 3223
    msgId:int
    parameters:str
    livingObject:int
    
    
