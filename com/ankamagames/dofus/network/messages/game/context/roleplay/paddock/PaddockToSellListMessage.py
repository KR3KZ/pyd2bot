from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockInformationsForSell import PaddockInformationsForSell


class PaddockToSellListMessage(NetworkMessage):
    protocolId = 3451
    pageIndex:int
    totalPage:int
    paddockList:PaddockInformationsForSell
    
