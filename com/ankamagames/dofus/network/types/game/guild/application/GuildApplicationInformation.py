from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.application.ApplicationPlayerInformation import ApplicationPlayerInformation


@dataclass
class GuildApplicationInformation(NetworkMessage):
    playerInfo:ApplicationPlayerInformation
    applyText:str
    creationDate:int
    
    
    def __post_init__(self):
        super().__init__()
    