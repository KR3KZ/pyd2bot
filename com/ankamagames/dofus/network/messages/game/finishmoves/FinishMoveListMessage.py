from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.finishmoves.FinishMoveInformations import FinishMoveInformations


class FinishMoveListMessage(NetworkMessage):
    finishMoves:list[FinishMoveInformations]
    
    
