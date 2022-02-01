from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation


class GameMapChangeOrientationsMessage(INetworkMessage):
    protocolId = 5656
    orientations:ActorOrientation
    
    
