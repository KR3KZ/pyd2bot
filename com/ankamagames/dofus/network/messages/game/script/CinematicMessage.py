from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CinematicMessage(INetworkMessage):
    protocolId = 5054
    cinematicId:int
    
    
