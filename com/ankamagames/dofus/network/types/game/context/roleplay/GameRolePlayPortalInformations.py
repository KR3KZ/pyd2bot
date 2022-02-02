from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.PortalInformation import PortalInformation


@dataclass
class GameRolePlayPortalInformations(GameRolePlayActorInformations):
    portal:PortalInformation
    
    
    def __post_init__(self):
        super().__init__()
    