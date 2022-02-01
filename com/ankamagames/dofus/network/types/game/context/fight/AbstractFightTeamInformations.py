from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractFightTeamInformations(NetworkMessage):
    teamId:int
    leaderId:int
    teamSide:int
    teamTypeId:int
    nbWaves:int
    
    
