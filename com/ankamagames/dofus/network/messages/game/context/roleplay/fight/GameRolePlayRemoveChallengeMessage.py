from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayRemoveChallengeMessage(INetworkMessage):
    protocolId = 5911
    fightId:int
    
    
