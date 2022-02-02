from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation


@dataclass
class GuildListApplicationModifiedMessage(NetworkMessage):
    apply:GuildApplicationInformation
    state:int
    playerId:int
    
    
    def __post_init__(self):
        super().__init__()
    