from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class GuildInvitedMessage(NetworkMessage):
    recruterId:int
    recruterName:str
    guildInfo:BasicGuildInformations
    
    
