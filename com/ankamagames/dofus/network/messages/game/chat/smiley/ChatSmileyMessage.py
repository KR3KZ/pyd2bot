from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChatSmileyMessage(INetworkMessage):
    protocolId = 5518
    entityId:int
    smileyId:int
    accountId:int
    
    
