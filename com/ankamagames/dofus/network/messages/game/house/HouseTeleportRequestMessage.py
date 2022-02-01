from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseTeleportRequestMessage(INetworkMessage):
    protocolId = 4012
    houseId:int
    houseInstanceId:int
    
    
