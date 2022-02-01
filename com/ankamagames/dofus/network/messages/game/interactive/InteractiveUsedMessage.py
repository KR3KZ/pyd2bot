from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InteractiveUsedMessage(NetworkMessage):
    entityId:int
    elemId:int
    skillId:int
    duration:int
    canMove:bool
    
    
