from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations


@dataclass
class SetCharacterRestrictionsMessage(NetworkMessage):
    actorId:int
    restrictions:ActorRestrictionsInformations
    
    
    def __post_init__(self):
        super().__init__()
    