from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective
from com.ankamagames.dofus.network.types.game.achievement.AchievementStartedObjective import AchievementStartedObjective


class Achievement(NetworkMessage):
    protocolId = 8621
    id:int
    finishedObjective:AchievementObjective
    startedObjectives:AchievementStartedObjective
    
