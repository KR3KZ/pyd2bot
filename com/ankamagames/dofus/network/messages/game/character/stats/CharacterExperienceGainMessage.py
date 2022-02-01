from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterExperienceGainMessage(NetworkMessage):
    experienceCharacter:int
    experienceMount:int
    experienceGuild:int
    experienceIncarnation:int
    
    
