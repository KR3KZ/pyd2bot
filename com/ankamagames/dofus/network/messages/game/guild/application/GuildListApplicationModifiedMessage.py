from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation


class GuildListApplicationModifiedMessage(NetworkMessage):
    protocolId = 8105
    apply:GuildApplicationInformation
    state:int
    playerId:int
    
