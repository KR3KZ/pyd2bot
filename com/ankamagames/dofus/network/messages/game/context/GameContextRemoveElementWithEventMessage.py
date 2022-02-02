from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveElementMessage import GameContextRemoveElementMessage


@dataclass
class GameContextRemoveElementWithEventMessage(GameContextRemoveElementMessage):
    elementEventId:int
    
    
    def __post_init__(self):
        super().__init__()
    