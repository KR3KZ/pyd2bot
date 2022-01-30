from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


class GameRolePlayNpcInformations(GameRolePlayActorInformations):
    protocolId = 7419
    npcId:int
    sex:bool
    specialArtworkId:int
    
