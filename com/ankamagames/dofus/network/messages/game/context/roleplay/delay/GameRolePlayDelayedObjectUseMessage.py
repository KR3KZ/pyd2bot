from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedActionMessage import GameRolePlayDelayedActionMessage


@dataclass
class GameRolePlayDelayedObjectUseMessage(GameRolePlayDelayedActionMessage):
    objectGID:int
    
    
    def __post_init__(self):
        super().__init__()
    