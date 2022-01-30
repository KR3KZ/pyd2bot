from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayNpcQuestFlag(NetworkMessage):
    protocolId = 3944
    questsToValidId:int
    questsToStartId:int
    
    
