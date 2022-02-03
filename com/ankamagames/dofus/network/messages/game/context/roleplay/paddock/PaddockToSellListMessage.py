from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockInformationsForSell import PaddockInformationsForSell
    


class PaddockToSellListMessage(NetworkMessage):
    pageIndex:int
    totalPage:int
    paddockList:list['PaddockInformationsForSell']
    

    def init(self, pageIndex:int, totalPage:int, paddockList:list['PaddockInformationsForSell']):
        self.pageIndex = pageIndex
        self.totalPage = totalPage
        self.paddockList = paddockList
        
        super().__init__()
    
    