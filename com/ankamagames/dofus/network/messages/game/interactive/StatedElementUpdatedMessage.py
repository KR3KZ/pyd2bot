from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement


class StatedElementUpdatedMessage(NetworkMessage):
    protocolId = 3961
    statedElement:StatedElement
    
