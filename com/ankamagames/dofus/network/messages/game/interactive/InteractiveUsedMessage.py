from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class InteractiveUsedMessage(NetworkMessage):
    protocolId = 4971
    entityId:int
    elemId:int
    skillId:int
    duration:int
    canMove:bool
    
    
