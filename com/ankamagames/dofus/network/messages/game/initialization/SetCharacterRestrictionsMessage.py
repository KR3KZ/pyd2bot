from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations


class SetCharacterRestrictionsMessage(NetworkMessage):
    actorId:int
    restrictions:ActorRestrictionsInformations
    
    
