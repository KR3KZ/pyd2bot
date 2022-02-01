from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations


class TaxCollectorMovementMessage(INetworkMessage):
    protocolId = 4589
    movementType:int
    basicInfos:TaxCollectorBasicInformations
    playerId:int
    playerName:str
    
    
