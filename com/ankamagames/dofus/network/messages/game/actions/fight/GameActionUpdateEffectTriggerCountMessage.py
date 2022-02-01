from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount


class GameActionUpdateEffectTriggerCountMessage(INetworkMessage):
    protocolId = 6461
    targetIds:GameFightEffectTriggerCount
    
    
