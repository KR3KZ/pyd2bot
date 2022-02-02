from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.guild.application.GuildPlayerApplicationAbstractMessage import GuildPlayerApplicationAbstractMessage


@dataclass
class GuildPlayerNoApplicationInformationMessage(GuildPlayerApplicationAbstractMessage):
    
    
    def __post_init__(self):
        super().__init__()
    