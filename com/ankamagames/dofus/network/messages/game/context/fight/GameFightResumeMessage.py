from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSpectateMessage import GameFightSpectateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown
    from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
    


class GameFightResumeMessage(GameFightSpectateMessage):
    spellCooldowns:list['GameFightSpellCooldown']
    summonCount:int
    bombCount:int
    

    def init(self, spellCooldowns:list['GameFightSpellCooldown'], summonCount:int, bombCount:int, effects:list['FightDispellableEffectExtendedInformations'], marks:list['GameActionMark'], gameTurn:int, fightStart:int, idols:list['Idol'], fxTriggerCounts:list['GameFightEffectTriggerCount']):
        self.spellCooldowns = spellCooldowns
        self.summonCount = summonCount
        self.bombCount = bombCount
        
        super().__init__(effects, marks, gameTurn, fightStart, idols, fxTriggerCounts)
    
    