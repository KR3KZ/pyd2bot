from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightLifePointsLostMessage import GameActionFightLifePointsLostMessage


@dataclass
class GameActionFightLifeAndShieldPointsLostMessage(GameActionFightLifePointsLostMessage):
    shieldLoss:int
    
    
    def __post_init__(self):
        super().__init__()
    