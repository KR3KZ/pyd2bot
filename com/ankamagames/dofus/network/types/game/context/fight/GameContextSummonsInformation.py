from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    


class GameContextSummonsInformation(NetworkMessage):
    spawnInformation:'SpawnInformation'
    wave:int
    look:'EntityLook'
    stats:'GameFightCharacteristics'
    summons:list['GameContextBasicSpawnInformation']
    

    def init(self, spawnInformation:'SpawnInformation', wave:int, look:'EntityLook', stats:'GameFightCharacteristics', summons:list['GameContextBasicSpawnInformation']):
        self.spawnInformation = spawnInformation
        self.wave = wave
        self.look = look
        self.stats = stats
        self.summons = summons
        
        super().__init__()
    
    