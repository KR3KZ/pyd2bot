from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective
    from com.ankamagames.dofus.network.types.game.achievement.AchievementStartedObjective import AchievementStartedObjective
    


class Achievement(NetworkMessage):
    id:int
    finishedObjective:list['AchievementObjective']
    startedObjectives:list['AchievementStartedObjective']
    

    def init(self, id:int, finishedObjective:list['AchievementObjective'], startedObjectives:list['AchievementStartedObjective']):
        self.id = id
        self.finishedObjective = finishedObjective
        self.startedObjectives = startedObjectives
        
        super().__init__()
    
    