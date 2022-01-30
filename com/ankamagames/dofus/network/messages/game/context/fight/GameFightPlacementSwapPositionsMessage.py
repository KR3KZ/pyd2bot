from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


class GameFightPlacementSwapPositionsMessage(NetworkMessage):
    protocolId = 995
    dispositions:list[IdentifiedEntityDispositionInformations]
    
