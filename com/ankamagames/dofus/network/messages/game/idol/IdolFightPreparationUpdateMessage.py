from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    


class IdolFightPreparationUpdateMessage(NetworkMessage):
    idolSource:int
    idols:list['Idol']
    

    def init(self, idolSource:int, idols:list['Idol']):
        self.idolSource = idolSource
        self.idols = idols
        
        super().__init__()
    
    