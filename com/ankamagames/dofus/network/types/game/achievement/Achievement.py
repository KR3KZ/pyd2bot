from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective
from com.ankamagames.dofus.network.types.game.achievement.AchievementStartedObjective import AchievementStartedObjective


class Achievement(INetworkMessage):
    protocolId = 8621
    id:int
    finishedObjective:AchievementObjective
    startedObjectives:AchievementStartedObjective
    
    
