from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaFightPropositionMessage(NetworkMessage):
    protocolId = 2533
    fightId:int
    alliesId:int
    duration:int
    
    
