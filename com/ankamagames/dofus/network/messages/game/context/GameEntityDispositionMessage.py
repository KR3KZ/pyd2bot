from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


class GameEntityDispositionMessage(NetworkMessage):
    protocolId = 8701
    disposition:IdentifiedEntityDispositionInformations
    
