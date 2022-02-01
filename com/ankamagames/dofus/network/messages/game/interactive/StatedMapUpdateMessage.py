from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement


class StatedMapUpdateMessage(NetworkMessage):
    statedElements:list[StatedElement]
    
    
