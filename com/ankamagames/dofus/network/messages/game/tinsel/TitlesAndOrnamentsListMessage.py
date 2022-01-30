from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TitlesAndOrnamentsListMessage(INetworkMessage):
    protocolId = 6204
    titles:int
    ornaments:int
    activeTitle:int
    activeOrnament:int
    
    
