from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot


@dataclass
class FightResultListEntry(NetworkMessage):
    outcome:int
    wave:int
    rewards:FightLoot
    
    
    def __post_init__(self):
        super().__init__()
    