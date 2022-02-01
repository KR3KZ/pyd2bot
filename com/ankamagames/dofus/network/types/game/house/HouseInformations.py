from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseInformations(INetworkMessage):
    protocolId = 3346
    houseId:int
    modelId:int
    
    
