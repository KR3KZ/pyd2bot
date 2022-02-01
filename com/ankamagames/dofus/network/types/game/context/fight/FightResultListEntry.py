from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot


class FightResultListEntry(INetworkMessage):
    protocolId = 6627
    outcome:int
    wave:int
    rewards:FightLoot
    
    
