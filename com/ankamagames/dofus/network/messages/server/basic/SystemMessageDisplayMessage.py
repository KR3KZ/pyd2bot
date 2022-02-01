from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SystemMessageDisplayMessage(NetworkMessage):
    hangUp:bool
    msgId:int
    parameters:list[str]
    
    
