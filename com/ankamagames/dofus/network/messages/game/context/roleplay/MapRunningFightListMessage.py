from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightExternalInformations import FightExternalInformations


@dataclass
class MapRunningFightListMessage(NetworkMessage):
    fights:list[FightExternalInformations]
    
    
    def __post_init__(self):
        super().__init__()
    