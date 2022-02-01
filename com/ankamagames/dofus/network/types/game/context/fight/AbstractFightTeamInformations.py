from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AbstractFightTeamInformations(INetworkMessage):
    protocolId = 3071
    teamId:int
    leaderId:int
    teamSide:int
    teamTypeId:int
    nbWaves:int
    
    
