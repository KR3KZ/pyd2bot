from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.ShowCellMessage import ShowCellMessage


@dataclass
class ShowCellSpectatorMessage(ShowCellMessage):
    playerName:str
    
    
    def __post_init__(self):
        super().__init__()
    