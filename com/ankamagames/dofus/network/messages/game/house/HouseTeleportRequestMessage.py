from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseTeleportRequestMessage(INetworkMessage):
    protocolId = 4012
    houseId:int
    houseInstanceId:int
    
    
