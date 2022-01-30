from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseGuildRightsViewMessage(NetworkMessage):
    protocolId = 7124
    houseId:int
    instanceId:int
    
