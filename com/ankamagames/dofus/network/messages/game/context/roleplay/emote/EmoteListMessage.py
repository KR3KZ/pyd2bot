from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EmoteListMessage(NetworkMessage):
    emoteIds:list[int]
    
    
