from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntDigRequestAnswerMessage import TreasureHuntDigRequestAnswerMessage


@dataclass
class TreasureHuntDigRequestAnswerFailedMessage(TreasureHuntDigRequestAnswerMessage):
    wrongFlagCount:int
    
    
    def __post_init__(self):
        super().__init__()
    