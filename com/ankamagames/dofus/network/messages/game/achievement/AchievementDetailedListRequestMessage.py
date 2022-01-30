from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AchievementDetailedListRequestMessage(INetworkMessage):
    protocolId = 5957
    categoryId:int
    
    
