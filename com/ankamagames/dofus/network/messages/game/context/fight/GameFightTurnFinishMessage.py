from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightTurnFinishMessage(INetworkMessage):
    protocolId = 6692
    isAfk:bool
    
    
