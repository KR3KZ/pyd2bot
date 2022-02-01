from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.application.ApplicationPlayerInformation import ApplicationPlayerInformation


class GuildApplicationInformation(NetworkMessage):
    playerInfo:ApplicationPlayerInformation
    applyText:str
    creationDate:int
    
    
