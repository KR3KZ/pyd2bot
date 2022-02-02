from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount


@dataclass
class GameFightSpectateMessage(NetworkMessage):
    effects:list[FightDispellableEffectExtendedInformations]
    marks:list[GameActionMark]
    gameTurn:int
    fightStart:int
    idols:list[Idol]
    fxTriggerCounts:list[GameFightEffectTriggerCount]
    
    
    def __post_init__(self):
        super().__init__()
    