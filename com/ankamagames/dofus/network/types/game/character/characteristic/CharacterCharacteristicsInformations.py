from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.alignment.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification


class CharacterCharacteristicsInformations(NetworkMessage):
    protocolId = 1918
    experience:float
    experienceLevelFloor:float
    experienceNextLevelFloor:float
    experienceBonusLimit:float
    kamas:float
    alignmentInfos:ActorExtendedAlignmentInformations
    criticalHitWeapon:int
    characteristics:list[CharacterCharacteristic]
    spellModifications:list[CharacterSpellModification]
    probationTime:int
    
