from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import GameFightMonsterInformations
from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


@dataclass
class GameFightMonsterWithAlignmentInformations(GameFightMonsterInformations):
    alignmentInfos:ActorAlignmentInformations
    
    
    def __post_init__(self):
        super().__init__()
    