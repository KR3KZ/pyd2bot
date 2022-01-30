from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations


class AlliancedGuildFactSheetInformations(GuildInformations):
    protocolId = 1714
    allianceInfos:BasicNamedAllianceInformations
    
    
