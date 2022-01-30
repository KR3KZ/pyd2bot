from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HavenBagFurnituresRequestMessage(INetworkMessage):
    protocolId = 8486
    cellIds:int
    funitureIds:int
    orientations:int
    
    
