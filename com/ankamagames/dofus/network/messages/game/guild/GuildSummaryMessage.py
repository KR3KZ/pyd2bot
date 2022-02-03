from com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
    


class GuildSummaryMessage(PaginationAnswerAbstractMessage):
    guilds:list['GuildFactSheetInformations']
    

    def init(self, guilds:list['GuildFactSheetInformations'], offset:int, count:int, total:int):
        self.guilds = guilds
        
        super().__init__(offset, count, total)
    
    