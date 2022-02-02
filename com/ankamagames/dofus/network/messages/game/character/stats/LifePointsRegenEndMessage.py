from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.character.stats.UpdateLifePointsMessage import UpdateLifePointsMessage


@dataclass
class LifePointsRegenEndMessage(UpdateLifePointsMessage):
    lifePointsGained:int
    
    
    def __post_init__(self):
        super().__init__()
    