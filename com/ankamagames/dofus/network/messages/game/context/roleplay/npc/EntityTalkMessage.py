from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityTalkMessage(NetworkMessage):
    entityId:int
    textId:int
    parameters:list[str]
    
    
