from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage


class TopTaxCollectorListMessage(AbstractTaxCollectorListMessage):
    protocolId = 3617
    isDungeon:bool
    
    
