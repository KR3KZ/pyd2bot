from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectMessageRequestMessage(NetworkMessage):
    msgId:int
    parameters:list[str]
    livingObject:int
    
    
