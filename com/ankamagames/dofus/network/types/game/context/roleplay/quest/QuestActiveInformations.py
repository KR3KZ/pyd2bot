from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestActiveInformations(INetworkMessage):
    protocolId = 1975
    questId:int
    
    
