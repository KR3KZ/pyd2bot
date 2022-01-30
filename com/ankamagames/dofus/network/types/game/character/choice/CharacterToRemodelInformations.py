from com.ankamagames.dofus.network.types.game.character.choice.CharacterRemodelingInformation import CharacterRemodelingInformation


class CharacterToRemodelInformations(CharacterRemodelingInformation):
    protocolId = 2646
    possibleChangeMask:int
    mandatoryChangeMask:int
    
