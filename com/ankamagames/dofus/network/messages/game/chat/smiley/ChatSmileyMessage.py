from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatSmileyMessage(NetworkMessage):
    protocolId = 5518
    entityId:int
    smileyId:int
    accountId:int
    
    
