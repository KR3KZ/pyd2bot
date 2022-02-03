from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ForgettableSpellItem import ForgettableSpellItem
    


class ForgettableSpellListUpdateMessage(NetworkMessage):
    action:int
    spells:list['ForgettableSpellItem']
    

    def init(self, action:int, spells:list['ForgettableSpellItem']):
        self.action = action
        self.spells = spells
        
        super().__init__()
    
    