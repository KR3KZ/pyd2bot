from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseGuildShareRequestMessage(NetworkMessage):
    protocolId = 5595
    houseId:int
    instanceId:int
    enable:bool
    rights:int
    
