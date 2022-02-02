from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellEffectMessage import GameActionFightDispellEffectMessage


@dataclass
class GameActionFightTriggerEffectMessage(GameActionFightDispellEffectMessage):
    
    
    def __post_init__(self):
        super().__init__()
    