from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NicknameRefusedMessage(INetworkMessage):
    protocolId = 2705
    reason:int
    
    
