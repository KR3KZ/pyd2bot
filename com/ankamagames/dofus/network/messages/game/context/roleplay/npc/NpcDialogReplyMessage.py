from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NpcDialogReplyMessage(INetworkMessage):
    protocolId = 398
    replyId:int
    
    
