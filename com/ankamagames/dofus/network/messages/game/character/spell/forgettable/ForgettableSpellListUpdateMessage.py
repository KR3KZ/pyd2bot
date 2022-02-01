from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ForgettableSpellItem import ForgettableSpellItem


class ForgettableSpellListUpdateMessage(NetworkMessage):
    action:int
    spells:list[ForgettableSpellItem]
    
    
