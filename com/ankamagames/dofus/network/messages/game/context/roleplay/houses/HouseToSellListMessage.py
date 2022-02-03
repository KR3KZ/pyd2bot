from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.HouseInformationsForSell import HouseInformationsForSell
    


class HouseToSellListMessage(NetworkMessage):
    pageIndex:int
    totalPage:int
    houseList:list['HouseInformationsForSell']
    

    def init(self, pageIndex:int, totalPage:int, houseList:list['HouseInformationsForSell']):
        self.pageIndex = pageIndex
        self.totalPage = totalPage
        self.houseList = houseList
        
        super().__init__()
    
    