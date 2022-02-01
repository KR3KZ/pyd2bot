from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem


class AllianceCreationValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    allianceEmblem:GuildEmblem
    
    
