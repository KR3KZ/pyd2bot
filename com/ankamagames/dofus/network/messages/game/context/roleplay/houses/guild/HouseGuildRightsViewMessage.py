from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseGuildRightsViewMessage(INetworkMessage):
    protocolId = 7124
    houseId:int
    instanceId:int
    
    
