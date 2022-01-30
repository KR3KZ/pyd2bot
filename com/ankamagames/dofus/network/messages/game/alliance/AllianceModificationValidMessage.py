from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class AllianceModificationValidMessage(NetworkMessage):
    protocolId = 4144
    allianceName:str
    allianceTag:str
    Alliancemblem:GuildEmblem
    
    
