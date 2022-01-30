from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations


class SetCharacterRestrictionsMessage(NetworkMessage):
    protocolId = 7853
    actorId:int
    restrictions:ActorRestrictionsInformations
    
