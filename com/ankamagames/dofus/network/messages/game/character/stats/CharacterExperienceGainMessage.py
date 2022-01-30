from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterExperienceGainMessage(NetworkMessage):
    protocolId = 4524
    experienceCharacter:float
    experienceMount:float
    experienceGuild:float
    experienceIncarnation:float
    
