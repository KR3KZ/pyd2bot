from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseGuildNoneMessage(NetworkMessage):
    protocolId = 9562
    houseId:int
    instanceId:int
    secondHand:bool
    
    
