from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


class GameEntitiesDispositionMessage(NetworkMessage):
    protocolId = 853
    dispositions:IdentifiedEntityDispositionInformations
    
    
