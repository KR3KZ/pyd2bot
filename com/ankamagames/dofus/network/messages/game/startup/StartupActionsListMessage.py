from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.startup.StartupActionAddObject import StartupActionAddObject
    


class StartupActionsListMessage(NetworkMessage):
    actions:list['StartupActionAddObject']
    

    def init(self, actions:list['StartupActionAddObject']):
        self.actions = actions
        
        super().__init__()
    
    