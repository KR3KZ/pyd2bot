from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayPlayerFightFriendlyRequestedMessage(INetworkMessage):
    protocolId = 2157
    fightId:int
    sourceId:int
    targetId:int
    
    
