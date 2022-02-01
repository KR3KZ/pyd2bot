from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo


class PrismsListMessage(NetworkMessage):
    prisms:list[PrismSubareaEmptyInfo]
    
    
