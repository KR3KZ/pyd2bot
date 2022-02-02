from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


@dataclass
class GameActionFightModifyEffectsDurationMessage(AbstractGameActionMessage):
    targetId:int
    delta:int
    
    
    def __post_init__(self):
        super().__init__()
    