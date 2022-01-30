from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LivingObjectMessageRequestMessage(INetworkMessage):
    protocolId = 3223
    msgId:int
    parameters:str
    livingObject:int
    
    
