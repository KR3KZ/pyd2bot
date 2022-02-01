from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildHouseRemoveMessage(INetworkMessage):
    protocolId = 1802
    houseId:int
    instanceId:int
    secondHand:bool
    
    
