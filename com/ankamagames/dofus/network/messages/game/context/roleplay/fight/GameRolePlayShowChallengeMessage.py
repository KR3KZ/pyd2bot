from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations


@dataclass
class GameRolePlayShowChallengeMessage(NetworkMessage):
    commonsInfos:FightCommonInformations
    
    
    def __post_init__(self):
        super().__init__()
    