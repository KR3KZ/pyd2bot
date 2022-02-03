from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayNpcQuestFlag(NetworkMessage):
    questsToValidId:list[int]
    questsToStartId:list[int]
    

    def init(self, questsToValidId:list[int], questsToStartId:list[int]):
        self.questsToValidId = questsToValidId
        self.questsToStartId = questsToStartId
        
        super().__init__()
    
    