from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NicknameChoiceRequestMessage(INetworkMessage):
    protocolId = 3297
    nickname:str
    
    
