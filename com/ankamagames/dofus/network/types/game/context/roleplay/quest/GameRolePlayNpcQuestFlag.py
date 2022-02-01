from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayNpcQuestFlag(NetworkMessage):
    questsToValidId:list[int]
    questsToStartId:list[int]
    
    
