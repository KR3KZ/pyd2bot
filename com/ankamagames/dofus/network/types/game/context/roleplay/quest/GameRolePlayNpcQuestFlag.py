from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayNpcQuestFlag(INetworkMessage):
    protocolId = 3944
    questsToValidId:int
    questsToStartId:int
    
    
