from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EmoteListMessage(INetworkMessage):
    protocolId = 9032
    emoteIds:int
    
    
