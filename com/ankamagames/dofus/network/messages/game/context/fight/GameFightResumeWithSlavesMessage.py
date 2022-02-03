from com.ankamagames.dofus.network.messages.game.context.fight.GameFightResumeMessage import GameFightResumeMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown
    from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
    


class GameFightResumeWithSlavesMessage(GameFightResumeMessage):
    slavesInfo:list['GameFightResumeSlaveInfo']
    

    def init(self, slavesInfo:list['GameFightResumeSlaveInfo'], spellCooldowns:list['GameFightSpellCooldown'], summonCount:int, bombCount:int, effects:list['FightDispellableEffectExtendedInformations'], marks:list['GameActionMark'], gameTurn:int, fightStart:int, idols:list['Idol'], fxTriggerCounts:list['GameFightEffectTriggerCount']):
        self.slavesInfo = slavesInfo
        
        super().__init__(spellCooldowns, summonCount, bombCount, effects, marks, gameTurn, fightStart, idols, fxTriggerCounts)
    
    