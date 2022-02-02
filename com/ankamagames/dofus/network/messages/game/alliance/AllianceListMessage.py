from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations


@dataclass
class AllianceListMessage(NetworkMessage):
    alliances:list[AllianceFactSheetInformations]
    
    
    def __post_init__(self):
        super().__init__()
    