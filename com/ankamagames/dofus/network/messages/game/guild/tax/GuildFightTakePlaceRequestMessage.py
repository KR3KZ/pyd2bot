from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightJoinRequestMessage import GuildFightJoinRequestMessage


@dataclass
class GuildFightTakePlaceRequestMessage(GuildFightJoinRequestMessage):
    replacedCharacterId:int
    
    
    def __post_init__(self):
        super().__init__()
    