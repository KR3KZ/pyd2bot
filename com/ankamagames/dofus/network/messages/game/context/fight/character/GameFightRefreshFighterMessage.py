from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations


class GameFightRefreshFighterMessage(NetworkMessage):
    protocolId = 6738
    informations:GameContextActorInformations
    
    
