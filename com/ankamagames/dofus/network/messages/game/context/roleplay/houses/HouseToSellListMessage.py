from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForSell import HouseInformationsForSell


class HouseToSellListMessage(INetworkMessage):
    protocolId = 4515
    pageIndex:int
    totalPage:int
    houseList:HouseInformationsForSell
    
    
