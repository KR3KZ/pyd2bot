from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class AllianceModificationEmblemValidMessage(NetworkMessage):
    protocolId = 8937
    Alliancemblem:GuildEmblem
    
