from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseGuildNoneMessage(INetworkMessage):
    protocolId = 9562
    houseId:int
    instanceId:int
    secondHand:bool
    
    
