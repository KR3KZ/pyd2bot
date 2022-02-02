from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


@dataclass
class AbstractGameActionFightTargetedAbilityMessage(AbstractGameActionMessage):
    targetId:int
    destinationCellId:int
    critical:int
    silentCast:bool
    verboseCast:bool
    
    
    def __post_init__(self):
        super().__init__()
    