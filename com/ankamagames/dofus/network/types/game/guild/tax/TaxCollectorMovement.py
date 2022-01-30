from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations


class TaxCollectorMovement(INetworkMessage):
    protocolId = 6775
    movementType:int
    basicInfos:TaxCollectorBasicInformations
    playerId:int
    playerName:str
    
    
