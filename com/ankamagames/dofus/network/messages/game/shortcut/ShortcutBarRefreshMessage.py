from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut
    


class ShortcutBarRefreshMessage(NetworkMessage):
    barType:int
    shortcut:'Shortcut'
    

    def init(self, barType:int, shortcut:'Shortcut'):
        self.barType = barType
        self.shortcut = shortcut
        
        super().__init__()
    
    