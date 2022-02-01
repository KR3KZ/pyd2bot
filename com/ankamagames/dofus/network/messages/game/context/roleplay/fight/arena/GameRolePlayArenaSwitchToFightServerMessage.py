from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayArenaSwitchToFightServerMessage(INetworkMessage):
    protocolId = 3316
    address:str
    ports:int
    ticket:int
    
    
