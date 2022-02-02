from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellMessage import GameActionFightDispellMessage


@dataclass
class GameActionFightDispellEffectMessage(GameActionFightDispellMessage):
    boostUID:int
    
    
    def __post_init__(self):
        super().__init__()
    