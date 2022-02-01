from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations


class TaxCollectorMovement(NetworkMessage):
    movementType:int
    basicInfos:TaxCollectorBasicInformations
    playerId:int
    playerName:str
    
    
