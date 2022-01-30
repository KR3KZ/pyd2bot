from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightRemoveTeamMemberMessage(NetworkMessage):
    protocolId = 6697
    fightId:int
    teamId:int
    charId:int
    
