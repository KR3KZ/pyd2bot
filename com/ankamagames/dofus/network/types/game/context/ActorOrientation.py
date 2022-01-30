from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ActorOrientation(INetworkMessage):
    protocolId = 6459
    id:int
    direction:int
    
    
