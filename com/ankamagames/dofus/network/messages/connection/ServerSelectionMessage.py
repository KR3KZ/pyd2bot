from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ServerSelectionMessage(NetworkMessage):
    protocolId = 214
    serverId:int
    
    
