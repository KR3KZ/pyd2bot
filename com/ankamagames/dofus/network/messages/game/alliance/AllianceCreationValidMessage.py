from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class AllianceCreationValidMessage(INetworkMessage):
    protocolId = 5504
    allianceName:str
    allianceTag:str
    allianceEmblem:GuildEmblem
    
    
