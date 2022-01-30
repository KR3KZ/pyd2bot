from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LivingObjectMessageMessage(NetworkMessage):
    protocolId = 2593
    msgId:int
    timeStamp:int
    owner:str
    objectGenericId:int
    
