from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayRemoveChallengeMessage(INetworkMessage):
    protocolId = 5911
    fightId:int
    
    
