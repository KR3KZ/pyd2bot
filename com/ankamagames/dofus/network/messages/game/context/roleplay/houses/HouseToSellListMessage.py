from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForSell import HouseInformationsForSell


class HouseToSellListMessage(NetworkMessage):
    pageIndex:int
    totalPage:int
    houseList:list[HouseInformationsForSell]
    
    
