from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class GuildApplicationIsAnsweredMessage(NetworkMessage):
    protocolId = 33
    accepted:bool
    guildInformation:GuildInformations
    
