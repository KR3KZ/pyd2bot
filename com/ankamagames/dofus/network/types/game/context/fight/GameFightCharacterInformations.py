from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


@dataclass
class GameFightCharacterInformations(GameFightFighterNamedInformations):
    level:int
    alignmentInfos:ActorAlignmentInformations
    breed:int
    sex:bool
    
    
    def __post_init__(self):
        super().__init__()
    