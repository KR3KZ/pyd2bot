from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo


class PrismsListMessage(INetworkMessage):
    protocolId = 3236
    prisms:PrismSubareaEmptyInfo
    
    
