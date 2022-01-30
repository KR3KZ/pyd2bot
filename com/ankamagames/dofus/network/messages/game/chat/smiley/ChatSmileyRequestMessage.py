from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChatSmileyRequestMessage(INetworkMessage):
    protocolId = 9062
    smileyId:int
    
    
