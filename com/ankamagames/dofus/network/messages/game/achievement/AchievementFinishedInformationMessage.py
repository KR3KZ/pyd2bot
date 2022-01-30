from com.ankamagames.dofus.network.messages.game.achievement.AchievementFinishedMessage import AchievementFinishedMessage


class AchievementFinishedInformationMessage(AchievementFinishedMessage):
    protocolId = 9768
    name:str
    playerId:int
    
