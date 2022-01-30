from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations


class GameContextMoveMultipleElementsMessage(INetworkMessage):
    protocolId = 2401
    movements:EntityMovementInformations
    
    
