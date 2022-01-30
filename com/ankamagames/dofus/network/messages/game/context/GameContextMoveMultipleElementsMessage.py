from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations


class GameContextMoveMultipleElementsMessage(NetworkMessage):
    protocolId = 2401
    movements:EntityMovementInformations
    
    
