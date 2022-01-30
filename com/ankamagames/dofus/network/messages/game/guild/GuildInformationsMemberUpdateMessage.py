from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildMember import GuildMember


class GuildInformationsMemberUpdateMessage(NetworkMessage):
    protocolId = 6301
    member:GuildMember
    
