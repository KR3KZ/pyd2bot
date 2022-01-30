from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import GameFightMonsterInformations
from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


class GameFightMonsterWithAlignmentInformations(GameFightMonsterInformations):
    protocolId = 108
    alignmentInfos:ActorAlignmentInformations
    
