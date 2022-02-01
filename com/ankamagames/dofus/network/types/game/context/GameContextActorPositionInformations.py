from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations


class GameContextActorPositionInformations(NetworkMessage):
    contextualId:int
    disposition:EntityDispositionInformations
    
    
