from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NotificationByServerMessage(NetworkMessage):
    id:int
    parameters:list[str]
    forceOpen:bool
    
    
