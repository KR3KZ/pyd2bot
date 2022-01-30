from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseTeleportRequestMessage(NetworkMessage):
    protocolId = 4012
    houseId:int
    houseInstanceId:int
    
    
