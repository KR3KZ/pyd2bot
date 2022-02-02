from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


@dataclass
class LockableStateUpdateStorageMessage(LockableStateUpdateAbstractMessage):
    mapId:int
    elementId:int
    
    
    def __post_init__(self):
        super().__init__()
    