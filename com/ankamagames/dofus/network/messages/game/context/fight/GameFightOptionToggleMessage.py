from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightOptionToggleMessage(INetworkMessage):
    protocolId = 2382
    option:int
    
    
