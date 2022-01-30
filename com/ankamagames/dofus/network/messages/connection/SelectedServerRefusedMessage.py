from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SelectedServerRefusedMessage(INetworkMessage):
    protocolId = 8116
    serverId:int
    error:int
    serverStatus:int
    
    
