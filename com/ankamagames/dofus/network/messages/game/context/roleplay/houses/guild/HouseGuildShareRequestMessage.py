from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseGuildShareRequestMessage(INetworkMessage):
    protocolId = 5595
    houseId:int
    instanceId:int
    enable:bool
    rights:int
    
    
