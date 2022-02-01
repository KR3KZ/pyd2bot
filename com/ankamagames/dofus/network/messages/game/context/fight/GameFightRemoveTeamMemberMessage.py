from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightRemoveTeamMemberMessage(NetworkMessage):
    fightId:int
    teamId:int
    charId:int
    
    
