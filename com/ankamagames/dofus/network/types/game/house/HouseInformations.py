from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseInformations(NetworkMessage):
    protocolId = 3346
    houseId:int
    modelId:int
    
