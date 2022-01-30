from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NotificationByServerMessage(NetworkMessage):
    protocolId = 2613
    id:int
    parameters:list[str]
    forceOpen:bool
    
