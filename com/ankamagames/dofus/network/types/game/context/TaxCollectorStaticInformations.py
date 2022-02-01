from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class TaxCollectorStaticInformations(INetworkMessage):
    protocolId = 4022
    firstNameId:int
    lastNameId:int
    guildIdentity:GuildInformations
    callerId:int
    
    
