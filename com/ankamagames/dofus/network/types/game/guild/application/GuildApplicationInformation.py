from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.application.ApplicationPlayerInformation import ApplicationPlayerInformation


class GuildApplicationInformation(INetworkMessage):
    protocolId = 7662
    playerInfo:ApplicationPlayerInformation
    applyText:str
    creationDate:int
    
    
