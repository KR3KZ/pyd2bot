from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NpcDialogQuestionMessage(NetworkMessage):
    protocolId = 8384
    messageId:int
    dialogParams:list[str]
    visibleReplies:list[int]
    
