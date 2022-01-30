from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayNpcQuestFlag(NetworkMessage):
    protocolId = 3944
    questsToValidId:list[int]
    questsToStartId:list[int]
    
