from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement


class InteractiveElementUpdatedMessage(INetworkMessage):
    protocolId = 7321
    interactiveElement:InteractiveElement
    
    
