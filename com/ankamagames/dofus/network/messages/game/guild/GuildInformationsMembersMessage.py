from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildMember import GuildMember


class GuildInformationsMembersMessage(NetworkMessage):
    protocolId = 3627
    members:GuildMember
    
