from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


@dataclass
class GameActionFightDispellableEffectMessage(AbstractGameActionMessage):
    effect:AbstractFightDispellableEffect
    
    
    def __post_init__(self):
        super().__init__()
    