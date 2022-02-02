from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol


@dataclass
class IdolPartyRefreshMessage(NetworkMessage):
    partyIdol:PartyIdol
    
    
    def __post_init__(self):
        super().__init__()
    