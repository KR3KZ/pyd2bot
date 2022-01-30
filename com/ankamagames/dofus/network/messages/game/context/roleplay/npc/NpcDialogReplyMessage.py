from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NpcDialogReplyMessage(INetworkMessage):
    protocolId = 398
    replyId:int
    
    
