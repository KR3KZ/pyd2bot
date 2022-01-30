from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NpcDialogQuestionMessage(INetworkMessage):
    protocolId = 8384
    messageId:int
    dialogParams:str
    visibleReplies:int
    
    
