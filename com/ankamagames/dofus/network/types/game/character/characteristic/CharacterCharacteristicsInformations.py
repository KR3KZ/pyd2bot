from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.alignment.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification
    


class CharacterCharacteristicsInformations(NetworkMessage):
    experience:int
    experienceLevelFloor:int
    experienceNextLevelFloor:int
    experienceBonusLimit:int
    kamas:int
    alignmentInfos:'ActorExtendedAlignmentInformations'
    criticalHitWeapon:int
    characteristics:list['CharacterCharacteristic']
    spellModifications:list['CharacterSpellModification']
    probationTime:int
    

    def init(self, experience:int, experienceLevelFloor:int, experienceNextLevelFloor:int, experienceBonusLimit:int, kamas:int, alignmentInfos:'ActorExtendedAlignmentInformations', criticalHitWeapon:int, characteristics:list['CharacterCharacteristic'], spellModifications:list['CharacterSpellModification'], probationTime:int):
        self.experience = experience
        self.experienceLevelFloor = experienceLevelFloor
        self.experienceNextLevelFloor = experienceNextLevelFloor
        self.experienceBonusLimit = experienceBonusLimit
        self.kamas = kamas
        self.alignmentInfos = alignmentInfos
        self.criticalHitWeapon = criticalHitWeapon
        self.characteristics = characteristics
        self.spellModifications = spellModifications
        self.probationTime = probationTime
        
        super().__init__()
    
    