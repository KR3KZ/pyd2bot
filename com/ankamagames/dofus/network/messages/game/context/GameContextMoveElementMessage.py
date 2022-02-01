from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations


class GameContextMoveElementMessage(NetworkMessage):
    movement:EntityMovementInformations
    
    
