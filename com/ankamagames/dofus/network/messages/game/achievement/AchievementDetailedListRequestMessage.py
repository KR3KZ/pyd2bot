from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AchievementDetailedListRequestMessage(INetworkMessage):
    protocolId = 5957
    categoryId:int
    
    
