from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MapFightCountMessage(INetworkMessage):
    protocolId = 9018
    fightCount:int
    
    
