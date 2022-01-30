from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LivingObjectMessageRequestMessage(NetworkMessage):
    protocolId = 3223
    msgId:int
    parameters:str
    livingObject:int
    
    
