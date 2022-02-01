from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class AllianceModificationValidMessage(INetworkMessage):
    protocolId = 4144
    allianceName:str
    allianceTag:str
    Alliancemblem:GuildEmblem
    
    
