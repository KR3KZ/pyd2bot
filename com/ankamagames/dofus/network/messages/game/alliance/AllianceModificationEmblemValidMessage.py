from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class AllianceModificationEmblemValidMessage(INetworkMessage):
    protocolId = 8937
    Alliancemblem:GuildEmblem
    
    
