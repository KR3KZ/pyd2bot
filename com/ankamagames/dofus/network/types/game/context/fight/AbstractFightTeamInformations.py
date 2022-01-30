from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AbstractFightTeamInformations(NetworkMessage):
    protocolId = 3071
    teamId:int
    leaderId:float
    teamSide:int
    teamTypeId:int
    nbWaves:int
    
