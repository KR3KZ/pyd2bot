from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement


class InteractiveMapUpdateMessage(NetworkMessage):
    protocolId = 8375
    interactiveElements:InteractiveElement
    
    
