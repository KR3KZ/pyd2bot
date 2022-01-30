from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayArenaSwitchToFightServerMessage(INetworkMessage):
    protocolId = 3316
    address:str
    ports:int
    ticket:int
    
    
