from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EmoteListMessage(INetworkMessage):
    protocolId = 9032
    emoteIds:int
    
    
