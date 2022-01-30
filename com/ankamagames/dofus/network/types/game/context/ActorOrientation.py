from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ActorOrientation(NetworkMessage):
    protocolId = 6459
    id:int
    direction:int
    
    
