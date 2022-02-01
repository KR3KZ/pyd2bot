from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportOnSameMapMessage(INetworkMessage):
    protocolId = 9521
    targetId:int
    cellId:int
    
    
