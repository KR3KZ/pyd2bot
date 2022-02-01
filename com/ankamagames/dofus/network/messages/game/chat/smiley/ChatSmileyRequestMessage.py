from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChatSmileyRequestMessage(INetworkMessage):
    protocolId = 9062
    smileyId:int
    
    
