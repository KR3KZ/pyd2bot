from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseBuyResultMessage(NetworkMessage):
    protocolId = 9533
    houseId:int
    instanceId:int
    realPrice:int
    
