from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatSmileyRequestMessage(NetworkMessage):
    protocolId = 9062
    smileyId:int
    
