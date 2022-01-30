from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


class GameEntityDispositionMessage(INetworkMessage):
    protocolId = 8701
    disposition:IdentifiedEntityDispositionInformations
    
    
