from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.finishmoves.FinishMoveInformations import FinishMoveInformations


class FinishMoveListMessage(INetworkMessage):
    protocolId = 596
    finishMoves:FinishMoveInformations
    
    
