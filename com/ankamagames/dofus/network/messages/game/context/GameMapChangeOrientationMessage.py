from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation


class GameMapChangeOrientationMessage(NetworkMessage):
    protocolId = 595
    orientation:ActorOrientation
    
    
