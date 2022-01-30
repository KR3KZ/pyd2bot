from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation


class GameMapChangeOrientationsMessage(NetworkMessage):
    protocolId = 5656
    orientations:ActorOrientation
    
    
