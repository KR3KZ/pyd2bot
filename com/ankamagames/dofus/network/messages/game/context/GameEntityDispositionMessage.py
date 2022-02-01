from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


class GameEntityDispositionMessage(NetworkMessage):
    disposition:IdentifiedEntityDispositionInformations
    
    
