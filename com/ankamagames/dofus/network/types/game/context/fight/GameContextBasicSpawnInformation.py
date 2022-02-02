from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations


@dataclass
class GameContextBasicSpawnInformation(NetworkMessage):
    teamId:int
    alive:bool
    informations:GameContextActorPositionInformations
    
    
    def __post_init__(self):
        super().__init__()
    