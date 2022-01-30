from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightTurnStartMessage(INetworkMessage):
    protocolId = 3772
    id:int
    waitTime:int
    
    
