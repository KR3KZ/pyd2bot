from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChatSmileyExtraPackListMessage(INetworkMessage):
    protocolId = 8664
    packIds:int
    
    
