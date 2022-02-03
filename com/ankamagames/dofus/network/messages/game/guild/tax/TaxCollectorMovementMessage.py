from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
    


class TaxCollectorMovementMessage(NetworkMessage):
    movementType:int
    basicInfos:'TaxCollectorBasicInformations'
    playerId:int
    playerName:str
    

    def init(self, movementType:int, basicInfos:'TaxCollectorBasicInformations', playerId:int, playerName:str):
        self.movementType = movementType
        self.basicInfos = basicInfos
        self.playerId = playerId
        self.playerName = playerName
        
        super().__init__()
    
    