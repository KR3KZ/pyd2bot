from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations


class GameFightRefreshFighterMessage(INetworkMessage):
    protocolId = 6738
    informations:GameContextActorInformations
    
    
