from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NpcDialogReplyMessage(NetworkMessage):
    protocolId = 398
    replyId:int
    
