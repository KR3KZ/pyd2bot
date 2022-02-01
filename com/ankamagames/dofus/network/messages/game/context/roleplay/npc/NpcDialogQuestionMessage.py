from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcDialogQuestionMessage(NetworkMessage):
    messageId:int
    dialogParams:list[str]
    visibleReplies:list[int]
    
    
