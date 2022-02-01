from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations


class GameContextMoveMultipleElementsMessage(NetworkMessage):
    movements:list[EntityMovementInformations]
    
    
