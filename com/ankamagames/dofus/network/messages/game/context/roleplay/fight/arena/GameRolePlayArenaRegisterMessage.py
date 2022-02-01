from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayArenaRegisterMessage(INetworkMessage):
    protocolId = 5010
    battleMode:int
    
    
