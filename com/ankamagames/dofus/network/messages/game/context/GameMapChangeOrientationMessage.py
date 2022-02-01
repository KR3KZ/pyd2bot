from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation


class GameMapChangeOrientationMessage(NetworkMessage):
    orientation:ActorOrientation
    
    
