from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSpectateMessage import GameFightSpectateMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown


@dataclass
class GameFightResumeMessage(GameFightSpectateMessage):
    spellCooldowns:list[GameFightSpellCooldown]
    summonCount:int
    bombCount:int
    
    
    def __post_init__(self):
        super().__init__()
    