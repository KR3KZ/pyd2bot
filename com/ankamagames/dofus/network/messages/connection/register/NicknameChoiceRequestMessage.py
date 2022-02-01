from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NicknameChoiceRequestMessage(INetworkMessage):
    protocolId = 3297
    nickname:str
    
    
