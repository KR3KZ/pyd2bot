from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NotificationByServerMessage(INetworkMessage):
    protocolId = 2613
    id:int
    parameters:str
    forceOpen:bool
    
    
