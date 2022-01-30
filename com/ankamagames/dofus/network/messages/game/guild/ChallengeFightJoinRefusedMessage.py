from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChallengeFightJoinRefusedMessage(INetworkMessage):
    protocolId = 2066
    playerId:int
    reason:int
    
    
