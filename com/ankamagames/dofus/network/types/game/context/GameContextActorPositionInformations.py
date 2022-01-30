from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations


class GameContextActorPositionInformations(NetworkMessage):
    protocolId = 1244
    contextualId:float
    disposition:EntityDispositionInformations
    
