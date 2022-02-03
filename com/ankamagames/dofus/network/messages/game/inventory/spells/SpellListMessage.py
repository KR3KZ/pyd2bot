from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
    


class SpellListMessage(NetworkMessage):
    spellPrevisualization:bool
    spells:list['SpellItem']
    

    def init(self, spellPrevisualization:bool, spells:list['SpellItem']):
        self.spellPrevisualization = spellPrevisualization
        self.spells = spells
        
        super().__init__()
    
    