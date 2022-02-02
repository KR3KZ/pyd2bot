from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage


@dataclass
class GuildListApplicationRequestMessage(PaginationRequestAbstractMessage):
    
    
    def __post_init__(self):
        super().__init__()
    