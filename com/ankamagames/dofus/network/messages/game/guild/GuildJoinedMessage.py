from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class GuildJoinedMessage(NetworkMessage):
    protocolId = 1218
    guildInfo:GuildInformations
    memberRights:int
    
    
