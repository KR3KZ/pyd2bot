from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectMessageMessage(NetworkMessage):
    msgId:int
    timeStamp:int
    owner:str
    objectGenericId:int
    
    
