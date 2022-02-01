from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSpectateMessage import GameFightSpectateMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown


class GameFightResumeMessage(GameFightSpectateMessage):
    spellCooldowns:list[GameFightSpellCooldown]
    summonCount:int
    bombCount:int
    
    
