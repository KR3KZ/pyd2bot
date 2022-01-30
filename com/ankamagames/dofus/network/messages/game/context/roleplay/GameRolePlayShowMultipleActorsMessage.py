from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations


class GameRolePlayShowMultipleActorsMessage(INetworkMessage):
    protocolId = 1377
    informationsList:GameRolePlayActorInformations
    
    
