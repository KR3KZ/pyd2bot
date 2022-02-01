from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectGroundAddedMessage(INetworkMessage):
    protocolId = 3936
    cellId:int
    objectGID:int
    
    
