from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class GuildListMessage(NetworkMessage):
    protocolId = 5503
    guilds:GuildInformations
    
    
