from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LivingObjectMessageMessage(INetworkMessage):
    protocolId = 2593
    msgId:int
    timeStamp:int
    owner:str
    objectGenericId:int
    
    
