from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.CurrentMapMessage import CurrentMapMessage


@dataclass
class CurrentMapInstanceMessage(CurrentMapMessage):
    instantiatedMapId:int
    
    
    def __post_init__(self):
        super().__init__()
    