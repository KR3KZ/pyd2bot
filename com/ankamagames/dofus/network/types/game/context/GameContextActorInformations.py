from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


@dataclass
class GameContextActorInformations(GameContextActorPositionInformations):
    look:EntityLook
    
    
    def __post_init__(self):
        super().__init__()
    