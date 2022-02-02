from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.prism.PrismsListMessage import PrismsListMessage


@dataclass
class PrismsListUpdateMessage(PrismsListMessage):
    
    
    def __post_init__(self):
        super().__init__()
    