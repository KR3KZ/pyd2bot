from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectGroundAddedMessage(NetworkMessage):
    protocolId = 3936
    cellId:int
    objectGID:int
    
