from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NamedPartyTeam(INetworkMessage):
    protocolId = 6995
    teamId:int
    partyName:str
    
    
