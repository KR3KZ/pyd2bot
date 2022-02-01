from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations


class GameContextMoveElementMessage(INetworkMessage):
    protocolId = 5628
    movement:EntityMovementInformations
    
    
