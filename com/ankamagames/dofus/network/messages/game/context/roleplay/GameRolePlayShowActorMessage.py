from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


class GameRolePlayShowActorMessage(NetworkMessage):
    informations:GameRolePlayActorInformations
    
    
