from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations


class GameFightRefreshFighterMessage(NetworkMessage):
    informations:GameContextActorInformations
    
    
