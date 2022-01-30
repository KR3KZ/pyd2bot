from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestActiveInformations(INetworkMessage):
    protocolId = 1975
    questId:int
    
    
