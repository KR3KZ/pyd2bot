from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation


class GameMapChangeOrientationsMessage(INetworkMessage):
    protocolId = 5656
    orientations:ActorOrientation
    
    
