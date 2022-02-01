from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildMember import GuildMember


class GuildInformationsMembersMessage(INetworkMessage):
    protocolId = 3627
    members:GuildMember
    
    
