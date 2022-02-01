from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NotificationByServerMessage(INetworkMessage):
    protocolId = 2613
    id:int
    parameters:str
    forceOpen:bool
    
    
