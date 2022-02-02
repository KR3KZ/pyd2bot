from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations


@dataclass
class GameRolePlayActorInformations(GameContextActorInformations):
    
    
    def __post_init__(self):
        super().__init__()
    