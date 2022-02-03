from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown
    


class GameFightResumeSlaveInfo(NetworkMessage):
    slaveId:int
    spellCooldowns:list['GameFightSpellCooldown']
    summonCount:int
    bombCount:int
    

    def init(self, slaveId:int, spellCooldowns:list['GameFightSpellCooldown'], summonCount:int, bombCount:int):
        self.slaveId = slaveId
        self.spellCooldowns = spellCooldowns
        self.summonCount = summonCount
        self.bombCount = bombCount
        
        super().__init__()
    
    