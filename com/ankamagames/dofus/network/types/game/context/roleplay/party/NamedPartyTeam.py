from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NamedPartyTeam(INetworkMessage):
    protocolId = 6995
    teamId:int
    partyName:str
    
    
