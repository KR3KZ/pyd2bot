from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


class GameFightPlacementSwapPositionsMessage(INetworkMessage):
    protocolId = 995
    dispositions:list[IdentifiedEntityDispositionInformations]
    
    
