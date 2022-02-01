from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayArenaSwitchToGameServerMessage(INetworkMessage):
    protocolId = 651
    validToken:bool
    ticket:int
    homeServerId:int
    
    
