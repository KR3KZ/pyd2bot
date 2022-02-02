from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations


@dataclass
class GameFightRefreshFighterMessage(NetworkMessage):
    informations:GameContextActorInformations
    
    
    def __post_init__(self):
        super().__init__()
    