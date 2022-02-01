from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseGuildRightsViewMessage(INetworkMessage):
    protocolId = 7124
    houseId:int
    instanceId:int
    
    
