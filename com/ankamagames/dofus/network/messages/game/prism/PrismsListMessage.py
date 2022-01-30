from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo


class PrismsListMessage(NetworkMessage):
    protocolId = 3236
    prisms:list[PrismSubareaEmptyInfo]
    
