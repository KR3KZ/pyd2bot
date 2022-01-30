from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation


class GuildListApplicationModifiedMessage(INetworkMessage):
    protocolId = 8105
    apply:GuildApplicationInformation
    state:int
    playerId:int
    
    
