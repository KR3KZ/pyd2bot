from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableChangeCodeMessage import LockableChangeCodeMessage


@dataclass
class HouseLockFromInsideRequestMessage(LockableChangeCodeMessage):
    
    
    def __post_init__(self):
        super().__init__()
    