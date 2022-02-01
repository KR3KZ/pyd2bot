from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChatSmileyExtraPackListMessage(INetworkMessage):
    protocolId = 8664
    packIds:int
    
    
