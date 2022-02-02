from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveMultipleElementsMessage import GameContextRemoveMultipleElementsMessage


@dataclass
class GameContextRemoveMultipleElementsWithEventsMessage(GameContextRemoveMultipleElementsMessage):
    elementEventIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    