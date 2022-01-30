from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildHouseRemoveMessage(NetworkMessage):
    protocolId = 1802
    houseId:int
    instanceId:int
    secondHand:bool
    
    
