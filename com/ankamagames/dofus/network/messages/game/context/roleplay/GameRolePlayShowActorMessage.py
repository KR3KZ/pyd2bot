from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


class GameRolePlayShowActorMessage(NetworkMessage):
    protocolId = 503
    informations:GameRolePlayActorInformations
    
    
