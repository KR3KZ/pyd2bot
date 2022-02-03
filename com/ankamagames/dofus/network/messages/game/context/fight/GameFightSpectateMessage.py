from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
    


class GameFightSpectateMessage(NetworkMessage):
    effects:list['FightDispellableEffectExtendedInformations']
    marks:list['GameActionMark']
    gameTurn:int
    fightStart:int
    idols:list['Idol']
    fxTriggerCounts:list['GameFightEffectTriggerCount']
    

    def init(self, effects:list['FightDispellableEffectExtendedInformations'], marks:list['GameActionMark'], gameTurn:int, fightStart:int, idols:list['Idol'], fxTriggerCounts:list['GameFightEffectTriggerCount']):
        self.effects = effects
        self.marks = marks
        self.gameTurn = gameTurn
        self.fightStart = fightStart
        self.idols = idols
        self.fxTriggerCounts = fxTriggerCounts
        
        super().__init__()
    
    