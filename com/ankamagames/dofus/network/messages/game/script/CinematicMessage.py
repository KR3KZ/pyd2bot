from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CinematicMessage(NetworkMessage):
    protocolId = 5054
    cinematicId:int
    
    
