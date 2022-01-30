from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForSell import HouseInformationsForSell


class HouseToSellListMessage(NetworkMessage):
    protocolId = 4515
    pageIndex:int
    totalPage:int
    houseList:HouseInformationsForSell
    
    
