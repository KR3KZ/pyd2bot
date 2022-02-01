from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown


class GameFightResumeSlaveInfo(NetworkMessage):
    slaveId:int
    spellCooldowns:list[GameFightSpellCooldown]
    summonCount:int
    bombCount:int
    
    
