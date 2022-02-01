from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class TaxCollectorAttackedResultMessage(INetworkMessage):
    protocolId = 7270
    deadOrAlive:bool
    basicInfos:TaxCollectorBasicInformations
    guild:BasicGuildInformations
    
    
