from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation


class GuildListApplicationModifiedMessage(NetworkMessage):
    apply:GuildApplicationInformation
    state:int
    playerId:int
    
    
