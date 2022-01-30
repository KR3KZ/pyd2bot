from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseBuyResultMessage(INetworkMessage):
    protocolId = 9533
    houseId:int
    instanceId:int
    realPrice:int
    secondHand:bool
    bought:bool
    
    
