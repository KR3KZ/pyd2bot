from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation


class GameRolePlayPrismInformations(GameRolePlayActorInformations):
    protocolId = 6265
    prism:PrismInformation
    
