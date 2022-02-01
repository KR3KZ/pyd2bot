from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.finishmoves.FinishMoveInformations import FinishMoveInformations


class FinishMoveListMessage(INetworkMessage):
    protocolId = 596
    finishMoves:FinishMoveInformations
    
    
