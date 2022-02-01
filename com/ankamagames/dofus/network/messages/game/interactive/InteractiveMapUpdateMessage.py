from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement


class InteractiveMapUpdateMessage(NetworkMessage):
    interactiveElements:list[InteractiveElement]
    
    
