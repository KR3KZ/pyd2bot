from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AchievementDetailedListRequestMessage(NetworkMessage):
    protocolId = 5957
    categoryId:int
    
