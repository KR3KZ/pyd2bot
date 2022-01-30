from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations


class SetCharacterRestrictionsMessage(INetworkMessage):
    protocolId = 7853
    actorId:int
    restrictions:ActorRestrictionsInformations
    
    
