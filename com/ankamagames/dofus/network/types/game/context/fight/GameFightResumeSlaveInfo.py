from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown


class GameFightResumeSlaveInfo(INetworkMessage):
    protocolId = 8117
    slaveId:int
    spellCooldowns:GameFightSpellCooldown
    summonCount:int
    bombCount:int
    
    
