from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


@dataclass
class GameRolePlayCharacterInformations(GameRolePlayHumanoidInformations):
    alignmentInfos:ActorAlignmentInformations
    
    
    def __post_init__(self):
        super().__init__()
    