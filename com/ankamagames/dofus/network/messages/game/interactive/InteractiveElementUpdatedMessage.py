from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement


class InteractiveElementUpdatedMessage(NetworkMessage):
    protocolId = 7321
    interactiveElement:InteractiveElement
    
