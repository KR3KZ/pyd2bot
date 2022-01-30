from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.application.ApplicationPlayerInformation import ApplicationPlayerInformation


class GuildApplicationInformation(NetworkMessage):
    protocolId = 7662
    playerInfo:ApplicationPlayerInformation
    applyText:str
    creationDate:int
    
