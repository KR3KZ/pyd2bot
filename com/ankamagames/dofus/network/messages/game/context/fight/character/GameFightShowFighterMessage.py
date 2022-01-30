from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


class GameFightShowFighterMessage(INetworkMessage):
    protocolId = 2781
    informations:GameFightFighterInformations
    
    
