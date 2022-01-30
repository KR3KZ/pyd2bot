from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


class GameEntitiesDispositionMessage(INetworkMessage):
    protocolId = 853
    dispositions:IdentifiedEntityDispositionInformations
    
    
