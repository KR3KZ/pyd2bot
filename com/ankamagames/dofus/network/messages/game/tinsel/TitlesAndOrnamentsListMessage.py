from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TitlesAndOrnamentsListMessage(NetworkMessage):
    protocolId = 6204
    titles:int
    ornaments:int
    activeTitle:int
    activeOrnament:int
    
    
