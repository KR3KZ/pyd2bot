from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations


@dataclass
class GameRolePlayMountInformations(GameRolePlayNamedActorInformations):
    ownerName:str
    level:int
    
    
    def __post_init__(self):
        super().__init__()
    