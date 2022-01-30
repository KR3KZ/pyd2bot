from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildMember import GuildMember


class GuildInformationsMemberUpdateMessage(INetworkMessage):
    protocolId = 6301
    member:GuildMember
    
    
