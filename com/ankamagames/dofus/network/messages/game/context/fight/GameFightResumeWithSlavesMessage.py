from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightResumeMessage import GameFightResumeMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo


@dataclass
class GameFightResumeWithSlavesMessage(GameFightResumeMessage):
    slavesInfo:list[GameFightResumeSlaveInfo]
    
    
    def __post_init__(self):
        super().__init__()
    