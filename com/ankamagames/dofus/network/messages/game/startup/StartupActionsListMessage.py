from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.startup.StartupActionAddObject import StartupActionAddObject


@dataclass
class StartupActionsListMessage(NetworkMessage):
    actions:list[StartupActionAddObject]
    
    
    def __post_init__(self):
        super().__init__()
    