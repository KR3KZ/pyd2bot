from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


@dataclass
class TaxCollectorStaticInformations(NetworkMessage):
    firstNameId:int
    lastNameId:int
    guildIdentity:GuildInformations
    callerId:int
    
    
    def __post_init__(self):
        super().__init__()
    