from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation


@dataclass
class GuildListApplicationAnswerMessage(PaginationAnswerAbstractMessage):
    applies:list[GuildApplicationInformation]
    
    
    def __post_init__(self):
        super().__init__()
    