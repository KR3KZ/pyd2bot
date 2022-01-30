from com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations


class GuildSummaryMessage(PaginationAnswerAbstractMessage):
    protocolId = 4399
    guilds:GuildFactSheetInformations
    
