from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


@dataclass
class GameActionFightSummonMessage(AbstractGameActionMessage):
    summons:list[GameFightFighterInformations]
    
    
    def __post_init__(self):
        super().__init__()
    