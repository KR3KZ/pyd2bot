from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation


class GameMapChangeOrientationMessage(INetworkMessage):
    protocolId = 595
    orientation:ActorOrientation
    
    
