from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ServerSelectionMessage(INetworkMessage):
    protocolId = 214
    serverId:int
    
    
