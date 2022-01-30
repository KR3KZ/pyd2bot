from com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpMessage import CharacterLevelUpMessage


class CharacterLevelUpInformationMessage(CharacterLevelUpMessage):
    protocolId = 2461
    name:str
    id:int
    
    
