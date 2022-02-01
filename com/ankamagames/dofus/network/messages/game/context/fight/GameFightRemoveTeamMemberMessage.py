from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightRemoveTeamMemberMessage(INetworkMessage):
    protocolId = 6697
    fightId:int
    teamId:int
    charId:int
    
    
