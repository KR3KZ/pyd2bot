from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TitlesAndOrnamentsListMessage(NetworkMessage):
    protocolId = 6204
    titles:list[int]
    ornaments:list[int]
    activeTitle:int
    activeOrnament:int
    
