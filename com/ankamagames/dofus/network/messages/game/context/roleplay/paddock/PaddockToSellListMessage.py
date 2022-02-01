from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockInformationsForSell import PaddockInformationsForSell


class PaddockToSellListMessage(NetworkMessage):
    pageIndex:int
    totalPage:int
    paddockList:list[PaddockInformationsForSell]
    
    
