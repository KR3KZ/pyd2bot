from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class GuildInvitedMessage(INetworkMessage):
    protocolId = 7582
    recruterId:int
    recruterName:str
    guildInfo:BasicGuildInformations
    
    
