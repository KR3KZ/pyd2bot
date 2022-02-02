from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations


@dataclass
class GuildInformationsPaddocksMessage(NetworkMessage):
    nbPaddockMax:int
    paddocksInformations:list[PaddockContentInformations]
    
    
    def __post_init__(self):
        super().__init__()
    