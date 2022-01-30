from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PlayerStatus(NetworkMessage):
    protocolId = 3077
    statusId:int
    
    
