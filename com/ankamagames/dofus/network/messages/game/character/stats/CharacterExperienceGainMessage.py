from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterExperienceGainMessage(NetworkMessage):
    experienceCharacter:int
    experienceMount:int
    experienceGuild:int
    experienceIncarnation:int
    

    def init(self, experienceCharacter:int, experienceMount:int, experienceGuild:int, experienceIncarnation:int):
        self.experienceCharacter = experienceCharacter
        self.experienceMount = experienceMount
        self.experienceGuild = experienceGuild
        self.experienceIncarnation = experienceIncarnation
        
        super().__init__()
    
    