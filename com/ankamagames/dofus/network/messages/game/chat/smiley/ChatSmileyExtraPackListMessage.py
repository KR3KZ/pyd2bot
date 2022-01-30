from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatSmileyExtraPackListMessage(NetworkMessage):
    protocolId = 8664
    packIds:int
    
