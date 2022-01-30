from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightOptionToggleMessage(NetworkMessage):
    protocolId = 2382
    option:int
    
    
