from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AbstractFightTeamInformations(INetworkMessage):
    protocolId = 3071
    teamId:int
    leaderId:int
    teamSide:int
    teamTypeId:int
    nbWaves:int
    
    
