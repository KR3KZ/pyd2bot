from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


@dataclass
class TaxCollectorAttackedResultMessage(NetworkMessage):
    deadOrAlive:bool
    basicInfos:TaxCollectorBasicInformations
    guild:BasicGuildInformations
    
    
    def __post_init__(self):
        super().__init__()
    