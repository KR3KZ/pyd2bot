from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class GuildApplicationIsAnsweredMessage(INetworkMessage):
    protocolId = 33
    accepted:bool
    guildInformation:GuildInformations
    
    
