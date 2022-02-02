from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage


@dataclass
class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
    memberId:int
    active:bool
    
    
    def __post_init__(self):
        super().__init__()
    