from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.finishmoves.FinishMoveInformations import FinishMoveInformations


class FinishMoveListMessage(NetworkMessage):
    protocolId = 596
    finishMoves:list[FinishMoveInformations]
    
