from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class TaxCollectorAttackedResultMessage(NetworkMessage):
    protocolId = 7270
    deadOrAlive:bool
    basicInfos:TaxCollectorBasicInformations
    guild:BasicGuildInformations
    
    
