from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class AllianceInformations(BasicNamedAllianceInformations):
    protocolId = 5338
    allianceEmblem:GuildEmblem
    
    
