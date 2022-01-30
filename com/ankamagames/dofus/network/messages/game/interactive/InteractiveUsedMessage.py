from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class InteractiveUsedMessage(INetworkMessage):
    protocolId = 4971
    entityId:int
    elemId:int
    skillId:int
    duration:int
    canMove:bool
    
    
