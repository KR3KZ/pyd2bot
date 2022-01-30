from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EmoteListMessage(NetworkMessage):
    protocolId = 9032
    emoteIds:list[int]
    
