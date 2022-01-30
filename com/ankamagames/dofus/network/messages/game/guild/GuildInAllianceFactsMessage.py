from com.ankamagames.dofus.network.messages.game.guild.GuildFactsMessage import GuildFactsMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


class GuildInAllianceFactsMessage(GuildFactsMessage):
    protocolId = 6925
    allianceInfos:BasicNamedAllianceInformations
    
