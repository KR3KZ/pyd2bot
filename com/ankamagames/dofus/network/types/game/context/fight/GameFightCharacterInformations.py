from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


class GameFightCharacterInformations(GameFightFighterNamedInformations):
    protocolId = 2405
    level:int
    alignmentInfos:ActorAlignmentInformations
    breed:int
    sex:bool
    
