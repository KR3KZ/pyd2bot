from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown


@dataclass
class GameFightResumeSlaveInfo(NetworkMessage):
    slaveId:int
    spellCooldowns:list[GameFightSpellCooldown]
    summonCount:int
    bombCount:int
    
    
    def __post_init__(self):
        super().__init__()
    