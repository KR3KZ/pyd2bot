from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatSmileyMessage(NetworkMessage):
    protocolId = 5518
    entityId:float
    smileyId:int
    accountId:int
    
