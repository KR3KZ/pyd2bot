from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations
    


class GuildInformationsPaddocksMessage(NetworkMessage):
    nbPaddockMax:int
    paddocksInformations:list['PaddockContentInformations']
    

    def init(self, nbPaddockMax:int, paddocksInformations:list['PaddockContentInformations']):
        self.nbPaddockMax = nbPaddockMax
        self.paddocksInformations = paddocksInformations
        
        super().__init__()
    
    