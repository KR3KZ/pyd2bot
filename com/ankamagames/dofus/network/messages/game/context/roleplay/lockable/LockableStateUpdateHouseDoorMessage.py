from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


@dataclass
class LockableStateUpdateHouseDoorMessage(LockableStateUpdateAbstractMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    
    
    def __post_init__(self):
        super().__init__()
    