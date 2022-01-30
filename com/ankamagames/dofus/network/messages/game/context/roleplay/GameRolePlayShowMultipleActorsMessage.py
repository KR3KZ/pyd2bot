from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


class GameRolePlayShowMultipleActorsMessage(NetworkMessage):
    protocolId = 1377
    informationsList:GameRolePlayActorInformations
    
