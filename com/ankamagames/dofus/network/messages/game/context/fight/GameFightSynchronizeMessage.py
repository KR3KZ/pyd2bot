from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


class GameFightSynchronizeMessage(INetworkMessage):
    protocolId = 3028
    fighters:GameFightFighterInformations
    
    