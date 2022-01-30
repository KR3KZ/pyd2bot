from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.PortalInformation import PortalInformation


class GameRolePlayPortalInformations(GameRolePlayActorInformations):
    protocolId = 8125
    portal:PortalInformation
    
    
