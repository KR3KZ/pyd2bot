from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


class GameRolePlayCharacterInformations(GameRolePlayHumanoidInformations):
    protocolId = 9532
    alignmentInfos:ActorAlignmentInformations
    
    