from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayArenaRegistrationWarningMessage(INetworkMessage):
    protocolId = 1528
    battleMode:int
    
    
