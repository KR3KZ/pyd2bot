from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayRemoveChallengeMessage(NetworkMessage):
    protocolId = 5911
    fightId:int
    
