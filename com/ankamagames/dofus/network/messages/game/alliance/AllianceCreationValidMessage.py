from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


@dataclass
class AllianceCreationValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    allianceEmblem:GuildEmblem
    
    
    def __post_init__(self):
        super().__init__()
    