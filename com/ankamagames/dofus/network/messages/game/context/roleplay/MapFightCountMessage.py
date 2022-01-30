from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MapFightCountMessage(NetworkMessage):
    protocolId = 9018
    fightCount:int
    
