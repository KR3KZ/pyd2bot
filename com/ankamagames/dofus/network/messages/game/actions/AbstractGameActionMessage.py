from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractGameActionMessage(NetworkMessage):
    actionId:int
    sourceId:int
    
    
