from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterMessage import GameFightShowFighterMessage


@dataclass
class GameFightShowFighterRandomStaticPoseMessage(GameFightShowFighterMessage):
    
    
    def __post_init__(self):
        super().__init__()
    