from com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation


class GuildListApplicationAnswerMessage(PaginationAnswerAbstractMessage):
    applies:list[GuildApplicationInformation]
    
    
