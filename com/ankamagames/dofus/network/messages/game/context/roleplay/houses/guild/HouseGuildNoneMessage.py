from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseGuildNoneMessage(INetworkMessage):
    protocolId = 9562
    houseId:int
    instanceId:int
    secondHand:bool
    
    
