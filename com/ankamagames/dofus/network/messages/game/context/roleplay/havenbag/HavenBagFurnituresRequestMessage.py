from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HavenBagFurnituresRequestMessage(NetworkMessage):
    protocolId = 8486
    cellIds:int
    funitureIds:int
    orientations:int
    
    
