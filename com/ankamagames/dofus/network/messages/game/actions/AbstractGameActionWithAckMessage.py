from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


@dataclass
class AbstractGameActionWithAckMessage(AbstractGameActionMessage):
    waitAckId:int
    
    
    def __post_init__(self):
        super().__init__()
    