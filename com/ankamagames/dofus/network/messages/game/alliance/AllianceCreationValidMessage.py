from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class AllianceCreationValidMessage(NetworkMessage):
    protocolId = 5504
    allianceName:str
    allianceTag:str
    allianceEmblem:GuildEmblem
    
