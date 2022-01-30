from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportOnSameMapMessage(NetworkMessage):
    protocolId = 9521
    targetId:int
    cellId:int
    
    
