from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HavenBagFurnitureInformation(INetworkMessage):
    protocolId = 3647
    cellId:int
    funitureId:int
    orientation:int
    
    
