from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HavenBagFurnitureInformation(NetworkMessage):
    protocolId = 3647
    cellId:int
    funitureId:int
    orientation:int
    
