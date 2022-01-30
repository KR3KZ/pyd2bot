from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


class GameRolePlayShowActorMessage(INetworkMessage):
    protocolId = 503
    informations:GameRolePlayActorInformations
    
    
