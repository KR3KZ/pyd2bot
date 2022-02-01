from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


class GameRolePlayShowMultipleActorsMessage(NetworkMessage):
    informationsList:list[GameRolePlayActorInformations]
    
    
