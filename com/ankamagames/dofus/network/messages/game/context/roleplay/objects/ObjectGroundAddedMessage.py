from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectGroundAddedMessage(INetworkMessage):
    protocolId = 3936
    cellId:int
    objectGID:int
    
    
