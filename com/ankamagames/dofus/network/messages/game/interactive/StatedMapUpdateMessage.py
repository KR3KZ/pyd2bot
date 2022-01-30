from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement


class StatedMapUpdateMessage(INetworkMessage):
    protocolId = 8689
    statedElements:StatedElement
    
    
