from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HavenBagFurnitureInformation(INetworkMessage):
    protocolId = 3647
    cellId:int
    funitureId:int
    orientation:int
    
    
