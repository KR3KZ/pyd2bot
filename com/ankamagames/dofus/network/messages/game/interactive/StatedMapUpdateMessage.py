from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement


class StatedMapUpdateMessage(NetworkMessage):
    protocolId = 8689
    statedElements:list[StatedElement]
    
