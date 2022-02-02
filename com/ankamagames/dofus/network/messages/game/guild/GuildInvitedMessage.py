from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


@dataclass
class GuildInvitedMessage(NetworkMessage):
    recruterId:int
    recruterName:str
    guildInfo:BasicGuildInformations
    
    
    def __post_init__(self):
        super().__init__()
    