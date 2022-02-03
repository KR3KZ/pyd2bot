from com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation
    


class GuildListApplicationAnswerMessage(PaginationAnswerAbstractMessage):
    applies:list['GuildApplicationInformation']
    

    def init(self, applies:list['GuildApplicationInformation'], offset:int, count:int, total:int):
        self.applies = applies
        
        super().__init__(offset, count, total)
    
    