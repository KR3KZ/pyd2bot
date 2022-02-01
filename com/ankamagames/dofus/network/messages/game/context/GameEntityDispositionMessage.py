from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


class GameEntityDispositionMessage(INetworkMessage):
    protocolId = 8701
    disposition:IdentifiedEntityDispositionInformations
    
    
