from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations


@dataclass
class GuildSummaryMessage(PaginationAnswerAbstractMessage):
    guilds:list[GuildFactSheetInformations]
    
    
    def __post_init__(self):
        super().__init__()
    