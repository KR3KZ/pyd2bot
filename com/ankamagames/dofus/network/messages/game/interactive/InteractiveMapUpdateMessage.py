from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement


class InteractiveMapUpdateMessage(INetworkMessage):
    protocolId = 8375
    interactiveElements:InteractiveElement
    
    
