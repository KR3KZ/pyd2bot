from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayPlayerLifeStatusMessage(INetworkMessage):
    protocolId = 7689
    state:int
    phenixMapId:int
    
    
