from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations


class TaxCollectorStaticInformations(NetworkMessage):
    protocolId = 4022
    firstNameId:int
    lastNameId:int
    guildIdentity:GuildInformations
    callerId:float
    
