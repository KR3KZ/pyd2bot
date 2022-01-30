from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseInformations(INetworkMessage):
    protocolId = 3346
    houseId:int
    modelId:int
    
    
