from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations


class GameContextActorPositionInformations(INetworkMessage):
    protocolId = 1244
    contextualId:int
    disposition:EntityDispositionInformations
    
    
