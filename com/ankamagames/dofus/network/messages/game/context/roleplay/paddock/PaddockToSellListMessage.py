from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockInformationsForSell import PaddockInformationsForSell


class PaddockToSellListMessage(INetworkMessage):
    protocolId = 3451
    pageIndex:int
    totalPage:int
    paddockList:PaddockInformationsForSell
    
    
