from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


@dataclass
class GameActionFightActivateGlyphTrapMessage(AbstractGameActionMessage):
    markId:int
    active:bool
    
    
    def __post_init__(self):
        super().__init__()
    