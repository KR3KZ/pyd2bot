from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NamedPartyTeam(NetworkMessage):
    protocolId = 6995
    teamId:int
    partyName:str
    
    
