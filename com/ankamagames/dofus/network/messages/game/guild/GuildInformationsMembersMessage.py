from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildMember import GuildMember


class GuildInformationsMembersMessage(NetworkMessage):
    members:list[GuildMember]
    
    
