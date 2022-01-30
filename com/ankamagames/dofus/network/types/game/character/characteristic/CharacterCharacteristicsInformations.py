from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.alignment.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification


class CharacterCharacteristicsInformations(INetworkMessage):
    protocolId = 1918
    experience:int
    experienceLevelFloor:int
    experienceNextLevelFloor:int
    experienceBonusLimit:int
    kamas:int
    alignmentInfos:ActorExtendedAlignmentInformations
    criticalHitWeapon:int
    characteristics:CharacterCharacteristic
    spellModifications:CharacterSpellModification
    probationTime:int
    
    
