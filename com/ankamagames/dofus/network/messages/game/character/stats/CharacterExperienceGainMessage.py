from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterExperienceGainMessage(NetworkMessage):
    protocolId = 4524
    experienceCharacter:int
    experienceMount:int
    experienceGuild:int
    experienceIncarnation:int
    
    
