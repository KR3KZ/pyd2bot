from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightTurnListMessage(INetworkMessage):
    protocolId = 7238
    ids:int
    deadsIds:int
    
    
