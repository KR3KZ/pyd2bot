from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CinematicMessage(INetworkMessage):
    protocolId = 5054
    cinematicId:int
    
    
