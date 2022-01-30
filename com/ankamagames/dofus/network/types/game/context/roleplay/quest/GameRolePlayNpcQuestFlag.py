from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayNpcQuestFlag(INetworkMessage):
    protocolId = 3944
    questsToValidId:int
    questsToStartId:int
    
    
