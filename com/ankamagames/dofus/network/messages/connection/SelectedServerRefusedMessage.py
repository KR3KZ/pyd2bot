from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SelectedServerRefusedMessage(NetworkMessage):
    protocolId = 8116
    serverId:int
    error:int
    serverStatus:int
    
    
