from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightOptionStateUpdateMessage(INetworkMessage):
    protocolId = 4608
    fightId:int
    teamId:int
    option:int
    state:bool
    
    
