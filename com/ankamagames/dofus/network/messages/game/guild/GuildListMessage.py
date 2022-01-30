from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class GuildListMessage(INetworkMessage):
    protocolId = 5503
    guilds:GuildInformations
    
    
