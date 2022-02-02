from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.alliance.AllianceListMessage import AllianceListMessage


@dataclass
class AlliancePartialListMessage(AllianceListMessage):
    
    
    def __post_init__(self):
        super().__init__()
    