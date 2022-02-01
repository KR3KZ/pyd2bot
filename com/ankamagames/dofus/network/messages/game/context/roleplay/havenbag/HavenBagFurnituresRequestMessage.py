from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HavenBagFurnituresRequestMessage(INetworkMessage):
    protocolId = 8486
    cellIds:int
    funitureIds:int
    orientations:int
    
    
