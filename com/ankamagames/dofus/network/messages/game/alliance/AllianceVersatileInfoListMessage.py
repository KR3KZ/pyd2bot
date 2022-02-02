from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceVersatileInformations import AllianceVersatileInformations


@dataclass
class AllianceVersatileInfoListMessage(NetworkMessage):
    alliances:list[AllianceVersatileInformations]
    
    
    def __post_init__(self):
        super().__init__()
    