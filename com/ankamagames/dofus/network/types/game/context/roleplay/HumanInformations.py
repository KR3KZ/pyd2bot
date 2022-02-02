from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


@dataclass
class HumanInformations(NetworkMessage):
    restrictions:ActorRestrictionsInformations
    sex:bool
    options:list[HumanOption]
    
    
    def __post_init__(self):
        super().__init__()
    