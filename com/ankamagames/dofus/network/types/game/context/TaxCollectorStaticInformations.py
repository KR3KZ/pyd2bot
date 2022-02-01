from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class TaxCollectorStaticInformations(NetworkMessage):
    firstNameId:int
    lastNameId:int
    guildIdentity:GuildInformations
    callerId:int
    
    
