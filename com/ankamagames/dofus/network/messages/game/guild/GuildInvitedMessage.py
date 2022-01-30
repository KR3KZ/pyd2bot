from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class GuildInvitedMessage(NetworkMessage):
    protocolId = 7582
    recruterId:float
    recruterName:str
    guildInfo:BasicGuildInformations
    
