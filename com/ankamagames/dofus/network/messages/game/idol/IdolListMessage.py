from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol


@dataclass
class IdolListMessage(NetworkMessage):
    chosenIdols:list[int]
    partyChosenIdols:list[int]
    partyIdols:list[PartyIdol]
    
    
    def __post_init__(self):
        super().__init__()
    