from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations


class GameContextMoveElementMessage(NetworkMessage):
    protocolId = 5628
    movement:EntityMovementInformations
    
    
